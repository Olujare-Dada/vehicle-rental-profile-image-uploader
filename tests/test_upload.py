import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.s3_operations import S3Operations
from models.DiskFileObject import DiskFileObject


USER_ID = 1

s3_operations = S3Operations(USER_ID)
file_object = DiskFileObject("test_images/Marrakech_Morocco.png")

url = s3_operations.upload_file(file_object)
print(url)
file_object.close()

