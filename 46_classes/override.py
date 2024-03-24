class ObjectCounter:
    num_instances = 0

    def __init__(self):
        ObjectCounter.num_instances += 1


one = ObjectCounter()
print(one.num_instances)

print(ObjectCounter.num_instances)

one.value = 42
print(one.value)

one.num_instances = 85
print(ObjectCounter.num_instances)
print(one.num_instances)

print(one.__class__.num_instances)
