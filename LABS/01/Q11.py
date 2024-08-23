m1=int(input("enter marks of first subject :"))
m2=int(input("enter marks of second subject :"))
m3=int(input("enter marks of third subject :"))
dict = {
    "Subject 1": m1,
    "Subject 2": m2,
    "Subject 3": m3
}
avg=(dict["Subject 1"]+dict["Subject 2"]+dict["Subject 3"])/3
print("Average Marks : ",avg)

totalmarks=300
percentage=((dict["Subject 1"]+dict["Subject 2"]+dict["Subject 3"])/totalmarks)*100
print("Percentage : ",percentage)
