from enum import Enum

class Size(int, Enum):
    S = 1
    M = 2
    L = 3
    XL = 4


print(Size.S > Size.M)
print(Size.S < Size.M)
print(Size.L >= Size.M)
print(Size.L <= Size.M)
print(Size.L > 2)
print(Size.M < 1)


# class MixinA:
#     def a(self):
#         print(f"MixinA: {self.value}")
#
# class MixinB:
#     def b(self):
#         print(f"MixinB: {self.value}")
#
# class ValidEnum(MixinA, MixinB, str, Enum):
#     MEMBER = "value"
#
# ValidEnum.MEMBER.a()  # Call .a() from MixinA
# ValidEnum.MEMBER.b()  # Call .b() from MixinB
# ValidEnum.MEMBER.upper()  # Call .upper() from str
# class WrongMixinOrderEnum(Enum, MixinA, MixinB):
#     MEMBER = "value"
#
# class TooManyDataTypesEnum(int, str, Enum):
#     MEMBER = "value"
