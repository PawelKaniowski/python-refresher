from enum import Enum, auto, unique


class Week(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


enu = Week

print(list(enu))
print(Week(1))
print(Week['MONDAY'])
print((Week.TUESDAY))
print(Week.TUESDAY.name)
print(Week.TUESDAY.value)


class Season(Enum):
    WIOSNA, LATO, JESIEN, ZIMA = range(1, 5)


print(list(Season))


class Grades(Enum):
    A = 100
    B = 80
    C = 70
    D = 60
    F = 50


class Size(Enum):
    S = 'small'
    M = ' medium'
    L = 'large'
    XL = 'extra_large'

for size in Size:
    print(size.name, "->", size.value)
for name in Size.__members__:
    print(name)
for name in Size.__members__.keys():
    print(name)
for member in Size.__members__.values():
    print(member)

class Przelacznik(Enum):
    WLACZONY = True
    WYLACZONY = False


HTTP = Enum('HTTPMethod', ['GET', 'POST', 'PUSH', 'DELETE', 'PATCH'])
print(list(HTTP))

HTTP101 = Enum('HTTPMethod', ['GET', 'POST', 'PUSH', 'DELETE', 'PATCH'], start=101)
print(list(HTTP101))

HTTPStatusCode = Enum(value='HTTPStatusCode',
                      names=[('OK', 200), ('CREATED', 201), ('NOT_FOUND', 404), ('SERVER_ERROR', 500), ])
print(list(HTTPStatusCode))

class Day(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = 3
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = 7
print(list(Day))

class CardinalDirection(Enum):
    def _generate_next_value_(name: str, start: int, count: int, last_values: list):
        return name[0]
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

print(list(CardinalDirection))

# @unique  # returns error when the same value is found
class OperatingSystem(Enum):
    UBUNTU = 'linux'
    MACOS = 'darwin'
    WINDOWS = 'win'
    DEBIAN = 'linux'

print(list(OperatingSystem))
print(list(OperatingSystem.__members__.items()))
print(OperatingSystem.MACOS in OperatingSystem)
print(OperatingSystem.DEBIAN not in OperatingSystem )

class Semaphore(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3
def handle_semaphore(light):
    if light is Semaphore.RED:
        print('You have to STOP')
    elif light is Semaphore.YELLOW:
        print("Light will change to red, be careful")
    elif light is Semaphore.GREEN:
        print('You can continue')

def handle_semaphore_case(light):
    match light:
        case Semaphore.RED:
            print('You have to STOP')
        case Semaphore.YELLOW:
            print("Light will change to red, be careful")
        case Semaphore.GREEN:
            print('You can continue')

handle_semaphore(Semaphore.RED)
handle_semaphore(Semaphore.YELLOW)
handle_semaphore_case(Semaphore.GREEN)

class Sort(Enum):
    ASCENDING = 1
    DESCENDING = 2
    def __call__(self,values):
        return sorted(values, reverse=self is Sort.DESCENDING)

numbers = [1, 32, 43, 1, 9, 543, 0, -3]

print(Sort.ASCENDING(numbers))
print(Sort.DESCENDING(numbers))