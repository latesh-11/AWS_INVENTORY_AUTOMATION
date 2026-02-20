# AWS Inventory Automation Tool

##  Overview

AWS Inventory Automation Tool is a Python-based automation utility that collects infrastructure metadata across AWS services and exports normalized inventory reports in JSON and CSV formats.

This tool is designed to:

* Provide centralized visibility of AWS resources
* Support DevOps auditing and compliance checks
* Enable cost optimization tracking
* Serve as a foundation for multi-account cloud governance

---

## Architecture

```
AWS Session
   ↓
Collectors (EC2 / S3 / RDS)
   ↓
Paginator (Reusable AWS pagination utility)
   ↓
Formatter (Schema normalization)
   ↓
Exporter (JSON / CSV output)
   ↓
Logs
```

The system follows separation of concerns:

* Collectors handle resource extraction
* Paginator handles AWS pagination
* Formatter standardizes output schema
* Exporter handles file output
* Logger handles structured logging

---

## Features

* ✅ EC2 instance inventory (ID, state, region, tags)
* ✅ S3 bucket inventory (name, region, encryption status)
* ✅ RDS instance inventory (identifier, engine, storage, tags)
* ✅ Reusable pagination utility
* ✅ Custom AWS exception handling
* ✅ Structured logging
* ✅ JSON export
* ✅ CSV export
* ✅ Output normalization layer

---

## Authentication

Uses AWS profile from:

```
~/.aws/credentials
```

Default session configuration:

```python
get_session(profile="temp-admin", region="eu-central-1")
```

You can modify `session_manager.py` to:

* Use environment credentials
* Use IAM roles
* Use AssumeRole for cross-account access

---

## Installation

### Create virtual environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Tool

```bash
python main.py
```

After execution, the following files will be generated:

```
inventory.json
inventory.csv
```

---

## Sample Output Schema

```json
[
  {
    "service": "ec2",
    "resource_id": "i-0123456789",
    "region": "eu-central-1",
    "tags": {
      "Environment": "Dev",
      "Owner": "TeamA"
    }
  }
]
```

---

## Engineering Highlights

* Abstract base collector pattern
* Centralized paginator wrapper
* Structured exception wrapping (`AwsException`)
* Normalized reporting schema
* Modular architecture for easy extension

---

## Future Enhancements

* Multi-region automatic discovery
* Multi-account AssumeRole support
* Retry & exponential backoff
* DynamoDB / PostgreSQL export
* Dashboard integration (Streamlit / Grafana)
* Slack/Email alert integration
* Tag compliance auditing
* Cost center aggregation

---

## Technologies Used

* Python 3.x
* boto3
* botocore
* AWS SDK
* CSV / JSON standard libraries

---

## Notes

* S3 bucket listing does not require pagination.
* EC2 and RDS inventory use paginated APIs.
* Ensure AWS profile has required IAM permissions:

  * `ec2:DescribeInstances`
  * `rds:DescribeDBInstances`
  * `s3:ListAllMyBuckets`
  * `s3:GetBucketLocation`

