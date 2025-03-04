from abc import ABC
from abc import abstractmethod

class AList[T](ABC):
    def __init__(self):
        super().__init__()
        self._size: int = 0

    #  Getters
    @property
    def size(self) -> int:
        return self._size

    @property.getter
    @abstractmethod
    def head(self)->T: pass

    @property.getter
    @abstractmethod
    def tail(self)->T: pass

    @abstractmethod
    def popFront()->T: pass

    @abstractmethod
    def popBack()->T: pass


    





