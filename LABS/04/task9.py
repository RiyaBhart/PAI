
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display_info(self):
        print("Student ID: ",self.student_id)
        print("Student Name: ",self.name)


class Marks(Student):
    def __init__(self, student_id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(student_id, name)  
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus

    def display_marks(self):
        print("Marks in Algorithms: ",self.marks_algo)
        print("Marks in Data Science: ",self.marks_dataScience)
        print("Marks in Calculus: ",self.marks_calculus)


class Result(Marks):
    def __init__(self, student_id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(student_id, name, marks_algo, marks_dataScience, marks_calculus) 
    def calculate_total_and_average(self):
        total_marks = self.marks_algo + self.marks_dataScience + self.marks_calculus
        average_marks = total_marks / 3
        print(f"Total Marks: {total_marks}")
        print(f"Average Marks: {average_marks:.2f}")


student1 = Result(63, "Riya", 91, 95, 98)


student1.display_info()


student1.display_marks()


student1.calculate_total_and_average()
