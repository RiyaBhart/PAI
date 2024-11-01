# Create a NumPy array with 25 values and calculate the 75th percentile.

import numpy as np

a = np.arange(1,26)
answer = np.percentile(a,75)
print("Array : ",a)
print("75 percentile : ",answer)