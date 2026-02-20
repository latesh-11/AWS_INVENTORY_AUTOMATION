from collectors.base_collector import BaseCollector
from utils.exceptions import AwsException
from utils.logger import logging 
from botocore.exceptions import ClientError
from utils.paginator import Paginator


class EC2Collector(BaseCollector):

    def collect(self):
        logging.info(f"Starting the EC2 collection in region: {self.region}")

        ec2 = self.session.client("ec2", region_name=self.region)
        inventory = []

        try:
            for reservation in Paginator.aws_paginator(
                ec2,
                "describe_instances",
                "Reservations"
            ):
                for instance in reservation.get("Instances" , []):

                    tags = {
                        t.get("key"): t.get("Value")
                        for t in instance.get("Tags", [])
                    }

                    inventory.append({
                        "service": "ec2",
                        "instance_id": instance.get("InstanceId"),
                        "state": instance.get("State", {}).get("Name"),
                        "region": self.region,
                        "tags": tags
                    })
            logging.info(f"Collected {len(inventory)} EC2 instances")
            return inventory
        except ClientError as e:
            logging.error("EC2 collection failed", exc_info=True)
            self.handle_aws_error("EC2 collection failed", e)
