import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]  
y2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]   


plt.plot(x, y1, color='pink', marker='*', label='Y1 Line')

plt.plot(x, y2, color='gray', marker='*', label='Y2 Line')

plt.title("Two Lines on One Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.legend(loc="lower right")

plt.show()
