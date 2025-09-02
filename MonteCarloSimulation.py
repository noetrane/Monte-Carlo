
import random  
import math
import matplotlib.pyplot as plt
import numpy as np
import time

start = time.perf_counter()

def estimate_pi(num_points):

    x_inside, y_inside = [], []
    x_outside, y_outside = [], []
    circle_points = 0
    points = []

    theta = np.linspace(0, 2*np.pi, 500)
    x_circle = np.cos(theta)
    y_circle = np.sin(theta)
    plt.plot(x_circle, y_circle, color="black", linewidth=0.5)


    for i in range(num_points):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        points.append([x,y])

        if x*x + y*y <= 1:
            circle_points += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    percentage_inside = circle_points / num_points
    pi_est = 4 * percentage_inside
    relative_error = abs(pi_est - math.pi) / math.pi
    accuracy = 1 - relative_error
    accuracy = max(0, accuracy)

    end = time.perf_counter()

    print(f"Estimate: {pi_est:.6f}, Accuracy: {accuracy*100:.2f}%")
    print(f"Elapsed: {end - start:.6f} seconds")
    
    if num_points < 1000000:
        plt.scatter(x_inside, y_inside, color="blue", s=5)
        plt.scatter(x_outside, y_outside, color="red", s=5)
        plt.gca().set_aspect("equal")
        plt.title(f"Monte Carlo π ({num_points} pts)  ·  Estimate: {pi_est:.6f}  ·  Accuracy: {accuracy*100:.2f}%")
        plt.show()

    return pi_est, accuracy




# Only runs when you run the file directly
if __name__ == "__main__":
    estimate_pi(1000)   # this actually calls your function


