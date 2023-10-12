"""  
Solutions to MA4_part2:Combine and compare NUMBA and C++ 
Student: Wenjie Ouyang  
Mail: wenjie.ouyang.9030@student.uu.se  
Reviewed by: Behnam  
Reviewed date: Oct 12th  
"""
import numba
import time
import matplotlib.pyplot as plt
from person import Person


@numba.jit(nopython=True)
def fibonacci_numba(n):
    if n <= 1:
        return n
    else:
        return fibonacci_numba(n - 1) + fibonacci_numba(n - 2)


num1_N = int(input('time from: '))
num2_N = int(input('time to: '))
value_N = list(range(num1_N, num2_N))
times_N = []
for n in value_N:
    start_time_N = time.perf_counter()
    result_N = fibonacci_numba(n)
    end_time_N = time.perf_counter()
    time_taken_N = end_time_N - start_time_N
    times_N.append(time_taken_N)
#!/usr/bin/env python3.9
num1_C = int(input('time from: '))
num2_C = int(input('time to: '))
value_C = list(range(num1_C, num2_C))
times_C = []
for n in value_C:
    f = Person(n)
    start_time_C = time.perf_counter()
    f.fibonacci()
    end_time_C = time.perf_counter()
    times_C.append(end_time_C - start_time_C)


def fib_py(n):
    if n <= 1:
        return n
    else:
        return fib_py(n - 1) + fib_py(n - 2)


num1_P = int(input('time from: '))
num2_P = int(input('time to: '))
value_P = list(range(num1_P, num2_P))
times_P = [0] * (num2_P - num1_P)
for i, n in enumerate(value_P):
    start_time_P = time.perf_counter()
    fib_py(n)
    end_time_P = time.perf_counter()
    times_P[i] = end_time_P - start_time_P


def main():
    plt.figure()
    plt.plot(value_P, times_P, marker='o',
             linestyle='-', label='Python', color='b')
    plt.plot(value_N, times_N, marker='o',
             linestyle='-', label='Numba', color='y')
    plt.plot(value_C, times_C, marker='o',
             linestyle='-', label='C++', color='r')
    plt.ylabel('Time (seconds)')
    plt.xlabel('n')
    plt.title('Calculation of the fibonacci')
    plt.legend(loc='upper right')
    plt.grid(True)
    file_name = input("Save the png file as: ")
    plt.savefig(file_name)

    # plt.savefig('MA4_2_Plot_n20to30.png')
    # plt.savefig('MA4_2_Plot_n30to45.png')
if __name__ == '__main__':
    main()
