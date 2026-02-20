from botocore.exceptions import ClientError
from utils.exceptions import AwsException 


class Paginator:

    @staticmethod
    def aws_paginator(client,method,key,**kwargs):
        try:
            paginator = client.get_paginator(method)

            for page in paginator.paginate(**kwargs):
                for item in page.get(key, []):
                    yield item 
        except ClientError as e:
            raise AwsException("AWS pagination failed", e)
        
        except Exception as e:
            raise AwsException("unexpected pagination error", e)