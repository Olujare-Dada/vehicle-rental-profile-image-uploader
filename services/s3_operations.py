import boto3
from botocore.exceptions import ClientError
from werkzeug.utils import secure_filename
from models.DiskFileObject import DiskFileObject
from models.InMemoryFileObject import InMemoryFileObject
from config.S3Credentials import S3Credentials




class S3Operations:
    def __init__(self, user_id: int):
        # Initialize S3 credentials
        self.s3_credentials = S3Credentials()
        # Initialize S3 client
        self.s3 = boto3.client('s3',
                  aws_access_key_id=self.s3_credentials.access_key,
                  aws_secret_access_key=self.s3_credentials.secret_key)
        # Set user ID
        self.user_id = user_id
        # Set user folder
        self.bucket_name = self.s3_credentials.bucket_name
        self.user_folder = self.s3_credentials.set_user_folder(self.user_id).user_folder

    def file_exists(self, filename: str) -> bool:
        try:
            self.s3.head_object(Bucket=self.bucket_name, Key=f"{self.user_folder}/{filename}")
            print(f"{self.user_folder}/{filename} exists in {self.bucket_name}")
            return True
        except ClientError as e:
            if e.response['Error']['Code'] == "404":
                print(f"{self.user_folder}/{filename} does NOT exist in {self.bucket_name}")
                return False
            else:
                raise e

    def upload_file(self, file_object: DiskFileObject | InMemoryFileObject) -> str:
        filename = secure_filename(file_object.filename)
        print(f"Uploading file: {filename} to bucket: {self.bucket_name} for user: {self.user_id}")
        user_folder = self.user_folder

        self.s3.upload_fileobj(file_object, self.bucket_name, f"{self.user_folder}/{filename}")
        url = f"https://{self.bucket_name}.s3.amazonaws.com/{self.user_folder}/{filename}"
        print(f"file: {file_object.filename} uploaded to s3")
        file_object.close()
        return url


    def delete_folder_contents(self, prefix: str) -> str:
        response = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix)

        if 'Contents' not in response:
            return False

        objects_to_delete = [{'Key': obj['Key']} for obj in response['Contents']]

        delete_response = self.s3.delete_objects(
                Bucket=self.bucket_name,
                Delete={'Objects': objects_to_delete}
            )

        deleted = delete_response.get('Deleted', [])
        return True


    def delete_file(self) -> None:
        response = self.delete_folder_contents(self.user_folder)
        if response:
                    print(f"Profile images for user {self.user_id} deleted from {self.bucket_name}")
        else:
            print(f"Profile images for user {self.user_id} does not exist in {self.bucket_name}")


    def edit_file(self, file_object: DiskFileObject | InMemoryFileObject) -> str:
        self.delete_file()
        url = self.upload_file(file_object)
        file_object.close()
        return url


