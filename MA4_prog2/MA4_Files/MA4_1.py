"""  
Solutions to MA4_part1  
Student: Wenjie Ouyang  
Mail: wenjie.ouyang.9030@student.uu.se  
Reviewed by: Behnam  
Reviewed date: Oct 12th  
"""
import random
import math
import matplotlib.pyplot as plt
from functools import reduce
import concurrent.futures
import time


def pi_forecast(n):
    i = 0
    x_in, y_in = [], []
    x_out, y_out = [], []
    for _ in range(n):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        distance = x**2 + y**2
        if distance <= 1:
            i += 1
            x_in.append(x)
            y_in.append(y)
        else:
            x_out.append(x)
            y_out.append(y)
    print("Number of points inside the circle:", i)
    approximation = 4 * i / n
    print("Approximation of π ≈", approximation)
    print("Built-in constant π (math.pi):", math.pi)
    plt.scatter(x_in, y_in, color='red', label='Inside Circle')
    plt.scatter(x_out, y_out, color='blue', label='Outside Circle')
    plt.axis('equal')
    plt.legend()
    # plt.savefig('circle_points.png')
    plt.show()


for n in [1000, 10000, 100000]:
    pi_forecast(n)


def hypersphere_volume(n, d):
    i = 0
    points = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    points_p2 = [map(lambda x: x**2, ii) for ii in points]
    points_sum = [reduce(lambda x, y: x+y, ii) for ii in points_p2]
    inside_points = list(filter(lambda x: x <= 1, points_sum))
    approximation = (len(inside_points) / n)*(2**d)
    # i = filter(lambda point: sum(x**2 for x in point) <= 1, points)
    # approximation = reduce(lambda acc: acc + 1, i) / n * (2**d)
    exact = reduce(lambda x, y: x * y, map(lambda x: math.pi **
                   (x / 2) / math.gamma(x / 2 + 1), [d]))
    return approximation, exact


approximation_1, exact_1 = hypersphere_volume(100000, 2)
print(f"Approximation: {approximation_1}")
print(f"Exact Volume: {exact_1}")

approximation_2, exact_2 = hypersphere_volume(100000, 11)
print(f"Approximation: {approximation_2}")
print(f"Exact Volume: {exact_2}")


def hypersphere_volume_process(n, d):
    i = 0
    points = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    points_p2 = [map(lambda x: x**2, ii) for ii in points]
    points_sum = [reduce(lambda x, y: x+y, ii) for ii in points_p2]
    inside_points = list(filter(lambda x: x <= 1, points_sum))
    approximation = (len(inside_points) / n)*(2**d)
    # i = filter(lambda point: sum(x**2 for x in point) <= 1, points)
    # approximation = reduce(lambda acc: acc + 1, i) / n * (2**d)
    # exact = reduce(lambda x, y: x * y, map(lambda x: math.pi ** (x / 2) / math.gamma(x / 2 + 1), [d]))
    return approximation


def single_point(d):
    point = [random.uniform(-1, 1) for _ in range(d)]
    return point


def is_inside(point):
    distance = sum(x**2 for x in point)
    return distance <= 1


def hypersphere_volume_update(n, d, num_processes):
    processes_size = n // num_processes
    process_numbers = num_processes*[processes_size]
    dim = num_processes*[d]
    # result = num_processes*[0]
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        result = executor.map(hypersphere_volume_process, process_numbers, dim)
        res_sum = 0
        for r in result:
            res_sum += r
        approximation = res_sum / num_processes
        exact = (math.pi**(d/2)) / math.gamma(d/2 + 1)
        return approximation, exact
        # for _ in range(num_processes):
        #     points = [single_point(d) for _ in range(processes_size)]
        #     i = sum(map(is_inside, points))
        #     t += i


def main():
    n = int(input("random points to generate(n): "))
    d = int(input("dimensions (d): "))
    num_processes = int(input("num_processes: "))
    start_time = time.perf_counter()
    approximation, exact = hypersphere_volume_update(n, d, num_processes)
    end_time = time.perf_counter()
    print(f"approximation: {approximation:.6f}")
    print(f"exact volume: {exact:.6f}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()


'''
Number of points inside the circle: 785
Approximation of π ≈ 3.14
Built-in constant π (math.pi): 3.141592653589793

Number of points inside the circle: 7817
Approximation of π ≈ 3.1268
Built-in constant π (math.pi): 3.141592653589793

Number of points inside the circle: 78617
Approximation of π ≈ 3.14468
Built-in constant π (math.pi): 3.141592653589793

Approximation: 3.14064
Exact Volume: 3.141592653589793

Approximation: 1.57696
Exact Volume: 1.8841038793898994

random points to generate(n): 1000000
dimensions (d): 11
num_processes: 1
approximation: 1.783808
exact volume: 1.884104
Time taken: 30.01 seconds

random points to generate(n): 1000000 
dimensions (d): 11 
num_processes: 10 
approximation: 1.888256 
exact volume: 1.884104 
Time taken: 2.06 seconds
'''
