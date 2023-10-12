import random
import math
import matplotlib.pyplot as plt

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
    #plt.savefig('circle_points.png')
    plt.show()

for n in [1000, 10000, 100000]:
    pi_forecast(n)