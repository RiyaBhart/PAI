class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Marks(Student):
    def __init__(self, name, id, a, ds, c):
        super().__init__(name, id) 
        self.marks_algo = a
        self.marks_datascience = ds
        self.marks_cal = c
        
    def displaymarks(self):
        print("Marks in Algo: ", self.marks_algo)
        print("Marks in Data Science: ", self.marks_datascience)
        print("Marks in Calculus: ", self.marks_cal)
        
class Result(Marks):
    def __init__(self, name, id, a, ds, c):
        super().__init__(name, id, a, ds, c)  
        
    def totalmarks(self):
        tm = self.marks_algo + self.marks_datascience + self.marks_cal
        avg = tm / 3 
        print("Total Marks: ", tm)
        print("Average Marks: ", avg)

M = Marks("Maria", 12, 100, 99, 98.5)
M.displaymarks()

R = Result("Maria", 12, 100, 99, 98.5)
R.totalmarks()
