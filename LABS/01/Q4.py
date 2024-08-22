inputlist = input("Enter a list of integers : ")

sum = 0

for i in inputlist:
    if i != ' ' : 
        sum +=int(i)

print("Sum of all given integers is : ",sum)
