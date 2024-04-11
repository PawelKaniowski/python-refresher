def f(*args):
    for i in args:
        print(i)

def g(**kwargs):
    for k, v in kwargs.items():
        print(k, '->', v)
