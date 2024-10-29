import matplotlib.pyplot as plt
cities = ["Karachi","Lahore","Hyderabad"]
population = [10000,7000,5000]
plt.xlabel("Cities")
plt.ylabel("Population")
plt.title("Cities And Population")
plt.barh(cities,population,color="skyblue")
plt.show()