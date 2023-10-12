import time
def fibonacci_py(n):
    if n <= 1:
        return n
    else:
        return fibonacci_py(n - 1) + fibonacci_py(n - 2)
n = int(input('number of Fibonacci: '))
result, times = fibonacci_py(n)
print(f"Fibonacci({n}) = {result}")
print(f"time: {times:.4f} seconds")
