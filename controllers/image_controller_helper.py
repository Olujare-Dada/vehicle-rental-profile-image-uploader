from enum import Enum
from models.InMemoryFileObject import InMemoryFileObject


class AllowedExtensions(Enum):
    PNG = 'png'
    JPG = 'jpg'
    JPEG = 'jpeg'
    GIF = 'gif'

class AllowedMimeTypes(Enum):
    IMAGE_PNG = 'image/png'
    IMAGE_JPG = 'image/jpg'
    IMAGE_JPEG = 'image/jpeg'
    IMAGE_GIF = 'image/gif'




def is_allowed_file(uploaded_file: InMemoryFileObject) -> bool:
    extension = uploaded_file.filename.rsplit('.', 1)[-1].lower()
    mime_type = uploaded_file.mimetype
    return extension in [ext.value for ext in AllowedExtensions] and mime_type in [mime.value for mime in AllowedMimeTypes]