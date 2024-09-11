class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_biodata(self):
        print("Name : ",self.name)
        print("Age : ",self.age)

o=Student("Riya",19)
o.print_biodata()
