#!/usr/bin/env python3.9
import time
import matplotlib.pyplot as plt
from person import Person
num1 = int(input('time from: '))
num2 = int(input('time to: '))
value = list(range(num1, num2))
times = []
for n in value:
	f = Person(n)
	start_time = time.perf_counter()
	f.fibonacci()
	end_time = time.perf_counter()
	times.append(end_time - start_time)
plt.figure(figsize=(10, 6))
plt.plot(value, times, label='C++', color='blue')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('C++ Fibonacci Calculation Time')
plt.legend()
plt.grid(True)
file_name = input("Save the png file as: ")
plt.savefig(file_name)
