import numpy as np
from scipy.integrate import dblquad

def integrand(y, x):
    return x**2 + y**2

volume, error = dblquad(integrand, 0, 1, lambda x: 0, lambda x: 1)
print(f'Volume under the surface z = x^2 + y^2 over 0 <= x, y <= 1: {volume:.4f}') 