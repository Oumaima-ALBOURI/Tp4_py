from abc import ABC, abstractmethod

class Forme(ABC):

    @abstractmethod
    def aire(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} – aire : {self.aire():.2f}"