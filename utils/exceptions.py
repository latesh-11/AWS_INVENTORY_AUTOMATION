from botocore.exceptions import ClientError

class AwsException(Exception):
    def __init__(self, error_message: str , error_details:ClientError):
        super().__init__(error_message)

        self.error_message = error_message
        self.error_details = error_details

        # extract AWS errors
        if isinstance(error_details, ClientError):
            error_info = error_details.response.get("Error", {})
            self.error_code = error_info.get("Code")
            self.aws_message = error_info.get("Message")
            self.request_id = error_details.response.get("ResponseMetadata", {}).get("RequestId")
            self.operation_name = error_details.operation_name
        else:
            self.error_code = None
            self.aws_message = None
            self.request_id = None
            self.operation_name = None

    def __str__(self):
        return (
            f"{self.error_message} | "
            f"AWS Code: {self.error_code} |"
            f"AWS Message: {self.aws_message} |"
            f"Operation: {self.operation_name} |"
            f"RequestID: {self.request_id}"            
        )