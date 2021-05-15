from selection import Selection
from command import Command
from undo_stack import UndoStack
from insert_command import InsertCommand
from tagcommand import TagCommand
from makebold_command import MakeBoldCommand
from makeitalic_command import MakeItalicCommand
from makeunderline_command import MakeUnderlineCommand
from exception import InvalidTextPositionError


class Editor:
    __text: str
    undo_stack: UndoStack

    def __init__(self, text: str):
        self.__text = text
        self.undo_stack = UndoStack()

    def get_text(self):
        return self.__text

    def select(self, start: int, end: int):
        if start > end or end >= len(self.__text):
            raise InvalidTextPositionError("Требуемая позиция в тексте недоступна")
        return Selection(start, end)

    def find(self, what: str, after_pos: int = -1):
        return self.__text.find(what, after_pos + 1)

    def insert(self, selection: Selection, what: str):
        insert = InsertCommand(selection, what)
        self.__text = insert.do(self.__text)
        self.undo_stack.push(insert)

    def make_bold(self, selection: Selection):
        bold = MakeBoldCommand(selection)
        self.__text = bold.do(self.__text)
        self.undo_stack.push(bold)

    def make_italic(self, selection: Selection):
        italic = MakeItalicCommand(selection)
        self.__text = italic.do(self.__text)
        self.undo_stack.push(italic)

    def make_underline(self, selection: Selection):
        underline = MakeUnderlineCommand(selection)
        self.__text = underline.do(self.__text)
        self.undo_stack.push(underline)

    def undo(self):
        cmd = self.undo_stack.pop()
        if cmd is not None:
            self.__text = cmd.undo(self.__text)


if __name__ == "__main__":
    text = input("Введите текст\n")
    ed = Editor(text)
    cmd = 0
    while cmd != 7:
        cmd = int(input(
            "Введите номер действия:\n вставить текст - 1\n выделить текст: полужирным - 2, курсивным - 3, почеркнутым "
            "- 4\n отменить действие - 5\n найти в тексте - 6\n закончить работу - 7\n"))
        if 1 <= cmd <= 4:
            start, end = map(int, input("Введите начало и конец фрагмента текста для работы\n").split(" "))
            sel = ed.select(start, end)
        if cmd == 1:
            what = input("Введите текст для вставки\n")
            ed.insert(sel, what)
        if cmd == 2:
            ed.make_bold(sel)
        if cmd == 3:
            ed.make_italic(sel)
        if cmd == 4:
            ed.make_underline(sel)
        if cmd == 5:
            ed.undo()
        if cmd == 6:
            what = input("Введите текст, который нужно искать\n")
            after_pos = int(
                input("Введите номер символа, с которого начать поиск. Если поиск с начала текста, то введите -1\n"))
            if ed.find(what, after_pos) == -1:
                print("Ничего не найдено\n")
            else:
                while ed.find(what, after_pos) != -1:
                    res = ed.find(what, after_pos)
                    after_pos = res + len(what) - 1
                    print("начало:", res, "конец:", after_pos)
                print("\n")
        print(ed.get_text())
