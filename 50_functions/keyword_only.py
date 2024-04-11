def oper(x, y, *, op='+'):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '/':
         return x / y
    else:
        return None