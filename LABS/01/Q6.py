sub1=input("enter first subject : ")
mark1=int(input("enter marks obtained in first subject : "))
sub2=input("enter second subject : ")
mark2=int(input("enter marks obtained in second subject : "))
sub3=input("enter third subject : ")
mark3=int(input("enter marks obtained in third subject : "))
dict={sub1:mark1,sub2:mark2,sub3:mark3}


avg = (dict[sub1]+dict[sub2]+dict[sub3])/3
print(avg)


if dict[sub1]>dict[sub2] and dict[sub1]>dict[sub3]:
    print("highest marks in",sub1)
elif dict[sub2]>dict[sub1] and dict[sub2]>dict[sub3]:
    print("highest marks in",sub2)
elif dict[sub3]>dict[sub1] and dict[sub3]>dict[sub2]:
    print("highest marks in",sub3)
