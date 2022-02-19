import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

def gradient_descent(x, y):
    m_curr = b_curr = 0
    cost_curr = cost_last = 0
    rate = 0.01
    n = len(x)
    plt.scatter(x, y, color='red', marker='+', linewidth='5')
    while True:
        y_predicted = m_curr * x + b_curr
        print(m_curr, b_curr, i)
        plt.plot(x, y_predicted, color='green')
        md = -(2 / n) * sum(x * (y - y_predicted))
        yd = -(2 / n) * sum(y - y_predicted)
        cost_curr = (1 / n) * sum((y - y_predicted) ** 2)
        if math.isclose(cost_curr, cost_last, abs_tol=1e-10):
            break

        m_curr = m_curr - rate * md
        b_curr = b_curr - rate * yd
        cost_last = cost_curr

    print(m_curr, b_curr, cost_curr)