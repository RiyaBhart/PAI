x=int(input("enter an integer: "))
y=int(input("enter another integer: "))
z=int(input("choose an operation :\n1.+\n2.-\n3.*\n4.divison\n"))
if(z==1):
    print(x--y)
elif(z==2):
    print(x-y)
elif(z==3):
    print(x*y)
elif(z==4):
    print(x/y)
else:
    print("incorrect choice")
