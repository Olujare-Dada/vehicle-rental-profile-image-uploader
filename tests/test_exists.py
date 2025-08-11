import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.s3_operations import S3Operations


USER_ID = 1
filename = "Marrakech_Morocco.png"
s3_operations = S3Operations(USER_ID)
print(s3_operations.file_exists(filename))





