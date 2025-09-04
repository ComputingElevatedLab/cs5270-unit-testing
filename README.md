# Math and AWS S3 Unit Testing (boto3)

## Install dependencies
```bash
pip install -r requirements.txt
```

## Run math utils tests
```bash
python -m unittest discover -s tests -p "test_math_utils.py" -v
```

## Run tests with moto
```bash
python -m unittest discover -s tests -p "test_s3_with_moto.py" -v
```

## Run all tests with unittest
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## Run all tests with pytest
```bash
pytest -v
```
