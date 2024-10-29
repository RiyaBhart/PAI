import matplotlib.pyplot as plt
genders = ["f","m","m","m","f","f","f","f"]
gender={"female":0,"male":0}
for g in genders:
    if g == "f":
        gender["female"]+=1
    elif g == "m":
        gender["male"]+=1
        
labels = gender.keys()
sizes = gender.values()

plt.pie(sizes,labels=labels,colors=["pink","blue"],autopct="%1.1f%%")
plt.show()