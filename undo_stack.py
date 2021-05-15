from typing import Optional
from command import Command


class UndoStack:
    cmd: list[Command]

    def __init__(self):
        self.cmd = []

    def push(self, command: Command):
        self.cmd.append(command)

    def pop(self) -> Optional[Command]:
        if len(self.cmd) != 0:
            return self.cmd.pop()
        else:
            return None
