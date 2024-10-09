# Create a multi-dimensional array of 3 rows and 3 columns having odd numbers from 1 to
# 19 including 1 and excluding 19. After that, iterate over this array to print all elements.
import numpy as np
arr = np.arange(1, 19, 2)
narr = arr.reshape(3, 3)
for i in narr:
    for j in i:
        print(j)

