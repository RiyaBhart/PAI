# Write a program to create numpy array or vector of all the even integers from 20 to 50
# exluding 20 and 50.

import numpy as np
arr = np.arange(20, 50, 2)
arr = arr[arr != 20]
narr= np.array(arr)
print(narr)
