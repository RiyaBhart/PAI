import matplotlib.pyplot as plt


math_marks = [78, 85, 62, 90, 88, 76, 95, 89, 68, 80]
science_marks = [82, 79, 74, 92, 86, 80, 94, 87, 70, 78]

plt.figure(figsize=(8, 6))
plt.scatter(math_marks, science_marks, color='b', marker='*', label="Student Scores")

plt.title("Comparison of Mathematics and Science Marks")
plt.xlabel("Mathematics Marks")
plt.ylabel("Science Marks")

plt.legend(loc="upper left")

plt.show()
