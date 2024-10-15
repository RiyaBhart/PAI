import numpy as np

newarr = np.random.choice([2, 5, 9, 10], size=(4, 4))
im = np.eye(4)
newarr = newarr * im
print("New array after multiplication with identity matrix:\n", newarr)
oddarr = np.arange(1,32, 2)
oddarr = np.reshape(oddarr, (4, 4))
print("\nOdd array:\n", oddarr)

newarr = newarr + oddarr
print("\nResult after adding newarr and oddarr:\n", newarr)
