from abc import ABC, abstractmethod
from command import Command
from selection import Selection
from undo_stack import UndoStack


class InsertCommand(Command, ABC):
    selection: Selection
    erased_text: str
    inserted_text: str

    def __init__(self, selection: Selection, what: str = ''):
        self.selection = selection
        self.inserted_text = what
        self.erased_text = ''

    def do(self, text: str) -> str:
        self.erased_text = text[self.selection.start: self.selection.end + 1]
        return text[:self.selection.start] + self.inserted_text + text[self.selection.end + 1:]

    def undo(self, text: str) -> str:
        l = len(self.inserted_text)
        return text[:self.selection.start] + self.erased_text + text[self.selection.start + l:]
