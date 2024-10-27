# Write a Python program to display a bar chart and a pie chart for student height data taken
# from your class. Use different color for each bar and take at least 20 students.

import matplotlib.pyplot as plt

studentnames = [
    "Riya","Rija","Rayyan","Muhammad","Ukkashah","Haris","Huzaifa","Hamza","Sabeeh","Amna","Ibrahim","Emaan","Eshaal","Simran","Shayan","Rehan","Areeba","Areesha","Ramsha","Javeria"
]
heights = [160, 155, 170, 165, 172, 168, 158, 174, 162, 169, 164, 160, 170, 167, 165, 159, 175, 168, 166, 161]

colors = [
    "blue", "orange", "green", "red", "purple", "brown", "pink", "gray", "olive", "cyan",
    "magenta", "yellow", "teal", "lightblue", "darkgreen", "lightgreen", "navy", "coral", "skyblue", "lime"
]

plt.figure(figsize=(12, 6))
plt.bar(studentnames, heights, color=colors)
plt.xlabel("Students")
plt.ylabel("Height (cm)")
plt.title("Student Heights - Bar Chart")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(heights, labels=studentnames, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Student Heights - Pie Chart")
plt.show()
