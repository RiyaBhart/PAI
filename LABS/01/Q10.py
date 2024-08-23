inputlist = input("Enter a list of integers: ").split()

inputlist = [int(x) for x in inputlist]

largestnum = 0

for i in inputlist[:]:
    if i>largestnum:
        largestnum=i
        
print("largest num is  : ",largestnum)
