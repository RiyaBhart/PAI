import numpy as np
arr = np.arange(1000)
avg = np.average(arr)
print("average : ",avg)

var = np.var(arr)
print("variance : ",var)

sd = np.std(arr)
print("standard deviation : ",sd)

with open("newfile.txt","w") as file:
    file.write(f"Average : {avg}\n")
    file.write(f"Standard Deviation : {sd}\n")
    file.write(f"Variance : {var}\n")
    
with open("newfile.txt","r") as file:
    a = file.read()

print("--------\nContent in File : \n",a)
