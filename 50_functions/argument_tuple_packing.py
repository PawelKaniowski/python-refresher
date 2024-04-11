def f(*args):
    print(args)
    print(type(args), len(args))
    for x in args:
        print(x)

def avg(*args):
    total = 0
    for i in args:
        total += i
    return total / len(args)
