# employee.py
from datetime import datetime

class Employee:
    company = "Sapkowski, Inc."

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = datetime.fromisoformat(value)

    def compute_age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year
        birthday = datetime(today.year, self.birth_date.month,
            self.birth_date.day)

        if today < birthday:
            return age - 1

        return age

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return f"{self.name} is {self.compute_age()} years old"

    def __repr__(self):
        return (
            "Employee("
            f"""name="{self.name}", """
            f"""birth_date="{self.birth_date.strftime('%Y-%m-%d')}")"""
        )
Pawel = Employee('Pawel', '1979-05-22')

print(Pawel.compute_age())
print((Pawel.compute_age()))

employee = {'name': 'Anna', 'birth_date': '1965-09-14'}

new_employe = Employee.from_dict(employee)
print(new_employe.name)
