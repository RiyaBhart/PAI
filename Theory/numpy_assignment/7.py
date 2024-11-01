# Create a NumPy array with 50 random values. Find the indices of the maximum and minimum
# values in the array.

import numpy as np

a = np.random.rand(50)
a= a.round(2)
print(a)

max_index = np.argmax(a)
print("Max Index : ",max_index)

min_index = np.argmin(a)
print("Minimum Index : ",min_index)