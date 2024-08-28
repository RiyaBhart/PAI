def find_maximum(*numbers):
    max=0
    for i in numbers:
        if i>max:
            max=i
    print("maximum number is : ",max)

find_maximum(2,30,4,5,10)
