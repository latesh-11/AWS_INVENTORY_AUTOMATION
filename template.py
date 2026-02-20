import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(message)s'
)

list_of_files = [
    "config/accounts.yaml",
    "config/settings.py",
    "sessions/session_manager.py",
    "collectors/ec2_collector.py",
    "collectors/s3_collector.py",
    "collectors/rds_collector.py",
    "collectors/base_collector.py",
    "utils/paginator.py",
    "utils/tagging.py",
    "utils/logger.py",
    "utils/exceptions.py",
    "output/exporter.py",
    "output/formatter.py",
    "main.py",
    "requirements.txt"
]

for file in list_of_files:
    filepath = Path(file)

    # Create directory if needed
    if filepath.parent != Path("."):
        filepath.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {filepath.parent}")

    # Create empty file if missing or empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
