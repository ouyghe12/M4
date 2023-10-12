import random
import math
import concurrent.futures
import time
from functools import reduce

def hypersphere_volume_process(n, d):
    i = 0
    points = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    
    points_p2 = [map(lambda x: x**2, ii) for ii in points]
    points_sum = [reduce(lambda x, y: x+y, ii) for ii in points_p2]
    inside_points = list(filter(lambda x : x <= 1, points_sum))
    approximation = (len(inside_points) / n)*(2**d)
    #i = filter(lambda point: sum(x**2 for x in point) <= 1, points)
    #approximation = reduce(lambda acc: acc + 1, i) / n * (2**d)
    #exact = reduce(lambda x, y: x * y, map(lambda x: math.pi ** (x / 2) / math.gamma(x / 2 + 1), [d]))

    return approximation

def single_point(d):
    point = [random.uniform(-1, 1) for _ in range(d)]
    return point

def is_inside(point):
    distance = sum(x**2 for x in point)
    return distance <= 1

def hypersphere_volume(n, d, num_processes):
    processes_size = n // num_processes
    t = 0
    process_numbers = num_processes*[processes_size]
    dim = num_processes*[d]
    #result = num_processes*[0]
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
    approximation, exact = hypersphere_volume(n, d, num_processes)     
    end_time = time.perf_counter()
    print(f"approximation: {approximation:.6f}")
    print(f"exact volume: {exact:.6f}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")     
        
    
if __name__ == "__main__":
    main()

    
'''
random points to generate(n): 10000000 
dimensions (d): 11 
num_processes: 1 
approximation: 1.888461 
exact volume: 1.884104 
Time taken: 59.56 seconds 
random points to generate(n): 10000000
dimensions (d): 11
num_processes: 10
approximation: 1.908326
exact volume: 1.884104
Time taken: 22.03 seconds
'''