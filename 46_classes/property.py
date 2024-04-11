class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f"{self.first} {self.last}"


geralt = Person("Geralt", "of Rivia")

print(geralt.first)

print(geralt.last)

print(geralt.full_name)
