import time
import matplotlib.pyplot as plt
def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n - 1) + fib_py(n - 2)
num1 = int(input('time from: '))
num2 = int(input('time to: '))
value = list(range(num1, num2))
times = [0] * (num2 - num1)
for i, n in enumerate(value):
	start_time = time.perf_counter()
	fib_py(n)
	end_time = time.perf_counter()
	times[i] = end_time - start_time
plt.plot(value, times, marker='o', linestyle='-', color='r')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Python Fibonacci Calculation Time')
plt.grid(True)
file_name = input("Save the png file as: ")
plt.savefig(file_name)
