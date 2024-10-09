# Create 3x3 matrix containing only even numbers. Multiply each element of this array with
# 4 and then multiply resultant matrix with 3x3 identity matrix (identity matrix should not be
# hardcoded).

import numpy as np
mat = np.arange(0,18,2)
mat = mat.reshape(3,3)
rmat = mat*4
im = np.eye(3)
rmat1 = rmat*im
print(rmat1)
