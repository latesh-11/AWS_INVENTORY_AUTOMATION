import json
import csv
from utils.logger import logging


class InventoryExporter:

    @staticmethod
    def export_json(data, filename="inventory.json"):
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        logging.info(f"Inventory exported to {filename}")

    @staticmethod
    def export_csv(data, filename="inventory.csv"):
        if not data:
            return

        keys = data[0].keys()

        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

        logging.info(f"Inventory exported to {filename}")