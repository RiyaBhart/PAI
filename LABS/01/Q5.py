inputlist = input("Enter a list of integers: ").split()

inputlist = [int(x) for x in inputlist]

num = int(input("Enter an integer: "))

for i in inputlist[:]:  
    if i < num: 
        inputlist.remove(i)


print("List is now:", inputlist)
