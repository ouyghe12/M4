import time
from person import Person
n = int(input('number of Fibonacci: '))
f = Person(n)
start_time = time.perf_counter()
fib_result = f.fibonacci()
end_time = time.perf_counter()
times = end_time - start_time
print(f"Fibonacci({n}) = {fib_result}")
print(f"Time = {times:.4f} seconds")

'''
Fibonacci(47) = -1323752223
Time = 47.3537 seconds
'''
