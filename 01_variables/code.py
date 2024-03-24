# -- Numbers and Floats --

x = 15
price = 9.99
print(id(price))

discount = 0.2

result = price * (1 - discount)

print(result)

# -- Strings --

name = "Rolf"
name = "Rolf"

print(name)
print(name * 2)

# -- Changing variables --
# Variables are names for values.

a = {'sss'}
b = a

# Here we've given the value '25' the names 'a' and 'b'.

print(id(a))
print(id(b))

b = 17

# Here we've given the value '17' the name 'b'. The name 'a' is still a name for '25'!

print(a)
print(b)
