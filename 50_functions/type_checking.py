def f(a: int, b: str, c: float):
    import inspect   #Inspect live objects
    args = inspect.getfullargspec(f).args
    annotations = inspect.getfullargspec(f).annotations
    for x in args:
        print(x, '->',
              'arg is', type(locals()[x]), ',',
                        #locals() returns symbol table as a dictionary
              'annotation is', annotations[x],
              '/', (type(locals()[x])) is annotations[x])