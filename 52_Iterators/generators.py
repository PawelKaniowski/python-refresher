def squared_generator(sequence):
    for item in sequence:
        yield item * item


squared_generator([1, 2, 3])

for num in squared_generator([1, 2, 3]):
    print(num)

squares = (i * i for i in (1, 2, 3, 4))
for num in squares:
    print(num)
    