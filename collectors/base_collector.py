from abc import ABC, abstractmethod
from botocore.exceptions import ClientError
from utils.exceptions import AwsException

class BaseCollector(ABC):
    def __init__(self, session ,region):
        self.session = session
        self.region = region

        @abstractmethod
        def collect(self):
            pass

        def handle_aws_error(self, message, error):
            raise AwsException(message, error)