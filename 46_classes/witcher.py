from employee import Employee
print(Employee.company)

geralt = Employee("Geralt of Rivia", "1986-12-01")

Employee(name="Geralt of Rivia", birth_date="1986-12-01")
print(geralt)

print(geralt.compute_age())

print(geralt.company)

data = {
    "name": "Yennefer of Vengerberg",
    "birth_date": "1993-01-31",
}
yen = Employee.from_dict(data)

Employee(name="Yennefer of Vengerberg", birth_date="1993-01-31")
print(yen)

