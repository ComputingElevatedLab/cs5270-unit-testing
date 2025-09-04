# aws_s3.py
"""Small S3 helper module with dependency injection for testability."""
from __future__ import annotations
import boto3
from botocore.exceptions import ClientError
from typing import Optional, List

def get_s3_client(region_name: Optional[str] = None):
    return boto3.client("s3", region_name=region_name)

def upload_text(bucket: str, key: str, text: str, s3=None) -> None:
    s3 = s3 or get_s3_client()
    s3.put_object(Bucket=bucket, Key=key, Body=text.encode("utf-8"))

def download_text(bucket: str, key: str, s3=None) -> str:
    s3 = s3 or get_s3_client()
    try:
        resp = s3.get_object(Bucket=bucket, Key=key)
    except ClientError as e:
        if e.response.get("Error", {}).get("Code") == "NoSuchKey":
            raise FileNotFoundError(f"s3://{bucket}/{key} not found") from e
        raise
    body = resp["Body"].read()
    return body.decode("utf-8")

def list_keys(bucket: str, prefix: str = "", s3=None) -> List[str]:
    s3 = s3 or get_s3_client()
    paginator = s3.get_paginator("list_objects_v2")
    keys: List[str] = []
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get("Contents", []) or []:
            keys.append(obj["Key"])
    return keys
