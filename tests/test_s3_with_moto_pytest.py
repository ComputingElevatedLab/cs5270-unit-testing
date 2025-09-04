import pytest
import boto3
from moto import mock_aws
from aws_s3 import upload_text, download_text, list_keys

BUCKET = "demo-bucket"

# s3_client is declared as fixture, this makes this object usable from other functions that name it as an argument
@pytest.fixture 
def s3_client():
    # Moto intercepts boto3 calls
    with mock_aws():
        s3 = boto3.client("s3", region_name="us-east-1")
        s3.create_bucket(Bucket=BUCKET)
        yield s3   # provide to tests

def test_upload_and_download(s3_client):
    upload_text(BUCKET, "folder/hello.txt", "hello moto", s3=s3_client)
    out = download_text(BUCKET, "folder/hello.txt", s3=s3_client)
    assert out == "hello moto"

def test_list_keys(s3_client):
    for i in range(3):
        upload_text(BUCKET, f"data/file_{i}.txt", f"payload {i}", s3=s3_client)
    keys = list_keys(BUCKET, prefix="data/", s3=s3_client)
    assert sorted(keys) == ["data/file_0.txt", "data/file_1.txt", "data/file_2.txt"]

def test_download_missing_raises(s3_client):
    with pytest.raises(FileNotFoundError):
        download_text(BUCKET, "missing.txt", s3=s3_client)
