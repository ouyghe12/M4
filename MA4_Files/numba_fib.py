import numba
import time
import matplotlib.pyplot as plt
@numba.jit(nopython=True)
def fibonacci_numba(n):
	if n <= 1:
		return n
	else:
		return fibonacci_numba(n - 1) + fibonacci_numba(n - 2)
num1 = int(input('time from: '))
num2 = int(input('time to: '))
value = list(range(num1, num2))
times = []
for n in value:
	start_time = time.perf_counter()
	result = fibonacci_numba(n)
	end_time = time.perf_counter()
	time_taken = end_time - start_time
	times.append(time_taken)
plt.plot(value, times, marker='o', linestyle='-', color='r')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('numba Fibonacci Calculation Time')
plt.grid(True)
file_name = input("Save the png file as: ")
plt.savefig(file_name)
