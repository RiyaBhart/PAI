import numpy as np 

a = np.random.randint(1,20,size=(2,2))
print(a)
det = np.linalg.det(a)
print(det)

if det!=0:
    inv = np.linalg.inv(a)
    print(inv)
else:
    print("Inverse Not Possible!")
