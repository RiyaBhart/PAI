import numpy as np

arr1 = np.random.randint(0, 10, size=(5, 3))  # Random integers between 0 and 9
print(arr1)

arr2 = np.random.randint(0,10,size=(3,2))
print(arr2)

newarr = np.dot(arr1,arr2)
print(newarr)
