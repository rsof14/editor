from abc import ABC, abstractmethod
from selection import Selection
from command import Command
from undo_stack import UndoStack


class TagCommand(Command, ABC):
    open_tag: str
    close_tag: str
    selection: Selection

    def __init__(self, selection: Selection, open_tag: str, close_tag: str):
        self.selection = selection
        self.open_tag = open_tag
        self.close_tag = close_tag

    def do(self, text: str) -> str:
        return (text[:self.selection.start] + self.open_tag + text[
                                                              self.selection.start:self.selection.end + 1] + self.close_tag +
                text[self.selection.end + 1:])

    def undo(self, text: str) -> str:
        text = text[:self.selection.start] + text[self.selection.start + 3: self.selection.end + 4] + text[
                                                                                                      self.selection.end + 8:]
        return text
