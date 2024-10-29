import matplotlib.pyplot as plt

ages = [30, 19, 20, 23, 22, 45, 70, 55, 43, 21, 56, 31, 34]

age_groups = {
    "18-25": 0,
    "26-30": 0,
    "31-35": 0,
    "35+": 0
}

for age in ages:
    if 18 <= age <= 25:
        age_groups["18-25"] += 1
    elif 26 <= age <= 30:
        age_groups["26-30"] += 1
    elif 31 <= age <= 35:
        age_groups["31-35"] += 1
    elif age >= 36:
        age_groups["35+"] += 1


labels = age_groups.keys()
sizes = age_groups.values()

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=['red', 'pink', 'blue', 'magenta'], autopct='%1.1f%%')
plt.title('Age Group Distribution')
plt.show()
