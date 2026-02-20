from utils.logger import logging
from collectors.base_collector import BaseCollector
from utils.paginator import Paginator
from botocore.exceptions import ClientError


class RDSCollector(BaseCollector):

    def collect(self):
        logging.info(f"Starting RDS collection in {self.region}")

        rds = self.session.client("rds", region_name=self.region)
        inventory = []

        try:
            for db in Paginator.aws_paginator(
                rds,
                "describe_db_instances",
                "DBInstances"
            ):

                tags_response = rds.list_tags_for_resource(
                    ResourceName=db["DBInstanceArn"]
                )

                tags = {
                    t.get("Key"): t.get("Value")
                    for t in tags_response.get("TagList", [])
                }

                inventory.append({
                    "service": "rds",
                    "db_identifier": db.get("DBInstanceIdentifier"),
                    "engine": db.get("Engine"),
                    "allocated_storage": db.get("AllocatedStorage"),
                    "region": self.region,
                    "tags": tags
                })

            logging.info(f"Collected {len(inventory)} RDS instances")

        except ClientError as e:
            logging.error("RDS collection failed", exc_info=True)
            self.handle_aws_error("RDS collection failed", e)

        return inventory