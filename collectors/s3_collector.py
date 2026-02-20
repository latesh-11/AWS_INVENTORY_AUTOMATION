from utils.logger import logging
from collectors.base_collector import BaseCollector
from botocore.exceptions import ClientError


class S3Collector(BaseCollector):

    def collect(self):
        logging.info("Starting S3 bucket inventory")

        s3 = self.session.client("s3")
        inventory = []

        try:
            response = s3.list_buckets()

            for bucket in response.get("Buckets", []):
                name = bucket["Name"]

                # Region lookup
                loc = s3.get_bucket_location(Bucket=name)
                region = loc.get("LocationConstraint") or "us-east-1"

                inventory.append({
                    "service": "s3",
                    "bucket_name": name,
                    "region": region
                })

        except ClientError as e:
            self.handle_aws_error("S3 bucket collection failed", e)

        return inventory