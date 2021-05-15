from abc import ABC

from tagcommand import TagCommand
from selection import Selection


class MakeUnderlineCommand(TagCommand, ABC):
    def __init__(self, sel: Selection):
        super().__init__(sel, "<u>", "</u>")
