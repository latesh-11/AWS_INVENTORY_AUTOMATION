from utils.logger import logging
from collectors.ec2_collector import EC2Collector
from collectors.s3_collector import S3Collector
from collectors.rds_collector import RDSCollector
from sessions.session_manager import get_session
from output.exporter import InventoryExporter
from output.formatter import normalize_inventory


def main():
    logging.info("Starting AWS Inventory Automation")

    # Create AWS session
    session = get_session()

    inventory_data = []

    try:
        # --- EC2 ---
        ec2_data = EC2Collector(session, "eu-central-1").collect()
        inventory_data.extend(ec2_data or [])

        # --- S3 (global service) ---
        s3_data = S3Collector(session, None).collect()
        inventory_data.extend(s3_data or [])

        # --- RDS ---
        rds_data = RDSCollector(session, "eu-central-1").collect()
        inventory_data.extend(rds_data or [])

    except Exception as e:
        logging.error("Inventory collection failed", exc_info=True)
        raise

    # Normalize data before export
    formatted_data = normalize_inventory(inventory_data)

    # Export outputs
    InventoryExporter.export_json(formatted_data)
    InventoryExporter.export_csv(formatted_data)

    logging.info("Inventory collection completed successfully")


if __name__ == "__main__":
    main()