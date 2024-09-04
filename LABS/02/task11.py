students = {}

def addgrade(studentname, grade):
    if studentname in students:
        students[studentname].append(grade)
    else:
        print("Student " + studentname + " does not exist.")

def calculateaverage(studentname):
    if studentname in students:
        grades = students[studentname]
        if grades:
            average = sum(grades) / len(grades)
            print("Average grade for " + studentname + ": " + "{:.2f}".format(average))
        else:
            print("No grades available for " + studentname + ".")
    else:
        print("Student " + studentname + " does not exist.")

def addstudent(studentname):
    if studentname not in students:
        students[studentname] = []
    else:
        print("Student " + studentname + " already exists.")

def removestudent(studentname):
    if studentname in students:
        del students[studentname]
    else:
        print("Student " + studentname + " does not exist.")


addstudent("Ahmed")
addgrade("Ahmed", 85)
addgrade("Ahmed", 90)
calculateaverage("Ahmed")
removestudent("Ahmed")

addstudent("Fatima")
addgrade("Fatima", 88)
addgrade("Fatima", 92)
calculateaverage("Fatima")
removestudent("Fatima")
