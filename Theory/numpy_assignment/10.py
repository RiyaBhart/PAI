# Implement a function that accepts a NumPy array and normalizes it (subtracts the mean and
# divides by the standard deviation). Apply this function to a sample array.
import numpy as np
a = np.arange(1,25)

def normalize(a):
    mean = a.mean()
    sd = np.std(a)
    normalize = (a-mean)/sd
    normalize = normalize.round(3)
    print("Normalized Array : ",normalize)

normalize(a)