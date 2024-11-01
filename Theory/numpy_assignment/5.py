# Create a NumPy array of 10 values and apply the square root function to each element.

import numpy as np

a = np.arange(1,11)
sqrt_arr = np.sqrt(a)
sqrtnew = np.round(sqrt_arr,2)
print(sqrtnew)