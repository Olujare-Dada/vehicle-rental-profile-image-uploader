from abc import ABC, abstractmethod

class AbstractFileObject(ABC):
    
    @abstractmethod
    def read(self, size=-1):
        pass

    @abstractmethod
    def seek(self, offset, whence=0):
        pass

    @abstractmethod
    def close(self):
        pass

    @property
    @abstractmethod
    def filename(self):
        pass
