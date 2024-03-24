from functools import lru_cache


def fibonacci_recursive(n):
    print("fibonacci_recursive called with n =", n)
    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci_recursive(n - 1) + \
        fibonacci_recursive(n - 2)

fibonacci_recursive(30)

@lru_cache(maxsize=None)
def fibonacci_recursive_optimized(n):
    print("fibonacci_recursive_optimized called with n =", n)
    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci_recursive_optimized(n - 1) + \
        fibonacci_recursive_optimized(n - 2)

# fibonacci_recursive_optimized(30)