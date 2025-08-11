class FileObject:
    def __init__(self, filepath: str):
        self.file = open(filepath, 'rb')
    
    @property
    def filename(self):
        return self.file.name.split('/')[-1]
    
    def read(self, size=-1):
        return self.file.read(size)
    
    def close(self):
        self.file.close()