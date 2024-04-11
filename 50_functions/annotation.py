def f(a: int, b: str) -> float:
    print(a, b)
    return(3.5)

def area(
    r: {
           'desc': 'radius of circle',
           'type': float
       }) -> \
       {
           'desc': 'area of circle',
           'type': float
       }:
    return 3.14159 * (r ** 2)