import matplotlib.pyplot as plt
flavours=["vanilla","strawberry","chocolate"]
scoops =[50,10,85]
plt.pie(scoops,labels=flavours,colors=["beige","pink","chocolate"],autopct="%d")
plt.show()
