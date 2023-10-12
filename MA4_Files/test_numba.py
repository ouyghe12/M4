import numba
import time
@numba.jit(nopython=True)
def fibonacci_numba(n):
	if n <= 1:
		return n
	else:
		return fibonacci_numba(n - 1) + fibonacci_numba(n - 2)
n = int(input('number of Fibonacci: '))
start_time = time.perf_counter()
result = fibonacci_numba(n)
end_time = time.perf_counter()
times = end_time - start_time
print(f"Fibonacci({n}) = {result}")
print(f"Time = {times:.4f} seconds")


'''
Fibonacci(47) = 2971215073
Time = 47.4953 seconds
'''
