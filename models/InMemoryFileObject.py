from models.AbstractFileObject import AbstractFileObject


class InMemoryFileObject(AbstractFileObject):
    def __init__(self, file_data: bytes):
        self.file_data = file_data
        self._filename = file_data.filename

    def read(self, size=-1):
        return self.file_data.read(size)

    def seek(self, offset, whence=0):
        return self.file_data.seek(offset, whence)

    def close(self):
        return self.file_data.close()

    @property
    def filename(self):
        return self._filename
    
    def __str__(self):
        return f"InMemoryFileObject(filename={self.filename}, size={len(self.file_data)})"
    
    def __repr__(self):
        return f"InMemoryFileObject(filename={self.filename}, size={len(self.file_data)})"
    
    def __eq__(self, other):
        return self.file_data == other.file_data
    
    def __ne__(self, other):
        return self.file_data != other.file_data
    
    def __hash__(self):
        return hash(self.file_data)
    
    def __len__(self):
        return len(self.file_data)
    