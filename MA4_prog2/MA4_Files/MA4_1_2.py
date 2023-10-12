import random
import math
from functools import reduce

def hypersphere_volume(n, d):
    i = 0
    points = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    
    points_p2 = [map(lambda x: x**2, ii) for ii in points]
    points_sum = [reduce(lambda x, y: x+y, ii) for ii in points_p2]
    inside_points = list(filter(lambda x : x <= 1, points_sum))
    approximation = (len(inside_points) / n)*(2**d)
    #i = filter(lambda point: sum(x**2 for x in point) <= 1, points)
    #approximation = reduce(lambda acc: acc + 1, i) / n * (2**d)
    exact = reduce(lambda x, y: x * y, map(lambda x: math.pi ** (x / 2) / math.gamma(x / 2 + 1), [d]))

    return approximation, exact

approximation_1, exact_1 = hypersphere_volume(100000, 2)
print(f"Approximation: {approximation_1}")
print(f"Exact Volume: {exact_1}")

approximation_2, exact_2 = hypersphere_volume(100000, 11)
print(f"Approximation: {approximation_2}")
print(f"Exact Volume: {exact_2}")