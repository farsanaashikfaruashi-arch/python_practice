from abc import ABC, abstractmethod
class Storage(ABC):
    @abstractmethod
    def save(self):
        pass
    @abstractmethod
    def load(self):
        pass
class FileStorage(Storage):
    def save(self):
        print("Saving file")
    def load(self):
        print("Loading file")
fs = FileStorage()
fs.save()
fs.load()
