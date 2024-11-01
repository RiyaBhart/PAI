#Create a one-dimensional NumPy array containing integers from 1 to 10. Compute the sum,
# mean, and product of the array.
import numpy as np
a = np.arange(1,11)
sum = a.sum()
mean = a.mean()
product = 1
for i in range(len(a)):
    product *=a[i]
print(a)
print("Sum : ",sum)
print("Mean : ",mean)
print("Product : ",product)
