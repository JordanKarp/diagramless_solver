from enum import Enum, auto


class Value(Enum):
    BLACK = auto()
    EMPTY = auto()
    ACROSS = auto()
    DOWN = auto()
    ACROSSDOWN = auto()
    UNKNOWN = auto()
    FINAL = auto()

    def __repr__(self):
        name = self.name.title()
        if name == 'Acrossdown':
            name = 'AcrossDown'
        return name

    def __str__(self):
        name = self.name.title()
        if name == 'Acrossdown':
            name = 'AcrossDown'
        return name


OPTIONS = {Value.ACROSS, Value.DOWN,
           Value.ACROSSDOWN, Value.BLACK, Value.EMPTY}

CLUES = {Value.ACROSS, Value.DOWN, Value.ACROSSDOWN}


SYMBOLS = {
    Value.BLACK: "\u2587",
    Value.EMPTY: '-',
    Value.ACROSS: 'A',
    Value.DOWN:  'D',
    Value.ACROSSDOWN: 'Z',
    Value.UNKNOWN: '_',
    Value.FINAL: 'Y'

}
