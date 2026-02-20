import boto3


def get_session(profile="temp-admin", region="eu-central-1"):
    return boto3.Session(
        profile_name=profile,
        region_name=region
    )