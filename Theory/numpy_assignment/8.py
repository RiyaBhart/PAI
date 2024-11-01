# Create a 3x3 matrix representing a system of linear equations. Use NumPy to solve the system
# and print the solution.

import numpy as np

a = np.array([[2, 3, 1], [4, 5, 6], [1, 2, 3]])
b = np.array([2, 1, 0])

sol = np.linalg.solve(a, b)
print("Solution:", sol)
