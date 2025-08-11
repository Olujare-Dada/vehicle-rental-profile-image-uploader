from models.AbstractFileObject import AbstractFileObject
import os


class DiskFileObject(AbstractFileObject):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file = open(file_path, 'rb')

    def read(self, size=-1):
        return self.file.read(size)

    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    
    def close(self):
        return self.file.close()
    
    @property
    def filename(self):
        return self.file_path.split('/')[-1]
    
    def __str__(self):
        return f"DiskFileObject(filename={self.filename}, size={os.path.getsize(self.file_path)}, location={self.file_path})"
    
    def __repr__(self):
        return f"DiskFileObject(filename={self.filename}, size={os.path.getsize(self.file_path)}, location={self.file_path})"
    
    def __eq__(self, other):
        return self.file_path == other.file_path
    
    def __ne__(self, other):
        return self.file_path != other.file_path