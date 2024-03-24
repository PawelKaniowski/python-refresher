from enum import IntEnum

class Size(IntEnum):
    S = 1
    M = 2
    L = 3
    XL = "4"


list(Size)


class Size(IntEnum):
    S = 1
    M = 2
    L = 3
    XL = "4.o"

Size.XL #cannot be converted