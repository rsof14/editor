from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def do(self, text: str):
        pass

    @abstractmethod
    def undo(self, text: str):
        pass


