from dotenv import load_dotenv
import os

load_dotenv()

class S3Credentials:
    def __init__(self):
        self.ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
        self.SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
        self.BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
        self.USER_FOLDER = os.getenv('USER_FOLDER')

    @property
    def access_key(self) -> str:
        return self.ACCESS_KEY

    @property
    def secret_key(self) -> str:
        return self.SECRET_KEY

    @property
    def bucket_name(self) -> str:
        return self.BUCKET_NAME

    @property
    def user_folder(self) -> str:
        return self.USER_FOLDER
    
    def set_user_folder(self, user_id: int) -> 'S3Credentials':
        self.USER_FOLDER = self.USER_FOLDER.format(user_id=user_id)
        return self

    def set_bucket_name(self, bucket_name: str) -> None:
        self.BUCKET_NAME = bucket_name
    
    def set_access_key(self, access_key: str) -> None:
        self.ACCESS_KEY = access_key
    
    def set_secret_key(self, secret_key: str) -> None:
        self.SECRET_KEY = secret_key
    
