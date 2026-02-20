def normalize_inventory(data):
    """
    Ensures consistent output format.
    """
    normalized = []

    for item in data:
        normalized.append({
            "service": item.get("service"),
            "resource_id": (
                item.get("instance_id")
                or item.get("bucket_name")
                or item.get("db_identifier")
            ),
            "region": item.get("region"),
            "tags": item.get("tags", {})
        })

    return normalized