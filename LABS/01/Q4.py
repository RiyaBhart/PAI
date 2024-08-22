# Even count 

inputlist = input("Enter a list of integers : ")

evencount = 0

for i in inputlist:
    if i != ' ' and int(i) % 2 == 0: 
        evencount += 1

print("Count of even numbers:", evencount)
