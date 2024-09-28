class Employee:
    def __init__(self,n,s):
        self.name=n
        self.salary=s
        self.bonus=0
    def calbonus(self):
        pass
    def getinfo(self):
        print("Name : ",self.name)
        print("Salary : ",self.salary)
    
class Manager(Employee):
    def __init__(self,n,s):
        super().__init__(n,s)
    def hire(self):
        print("the manager is hiring someone\n")
    def calbonus(self):
        self.bonus = 0.2*self.salary
    def getinfo(self):
        super().getinfo()
        print("Bonus of Manager : ",self.bonus)
class Developer(Employee):
    def __init__(self,n,s):
        super().__init__(n,s)
    def writecode(self):
        print("developer is writing code\n")
    def calbonus(self):
        self.bonus = 0.1*self.salary
    def getinfo(self):
        super().getinfo()
        print("Bonus of Developer : ",self.bonus)
class SeniorManager(Manager):
    def __init__(self,n,s):
        super().__init__(n,s)
    def calbonus(self):
        self.bonus = 0.3*self.salary
    def getinfo(self):
        super().getinfo()
        print("Bonus of Senior Manager : ",self.bonus)
    
E = Employee("",0)
M = Manager("Ray",100000)
D = Developer("Fia",200000)
SM = SeniorManager("Nia",150000)
M.hire()
M.calbonus()
SM.calbonus()
D.writecode()
D.calbonus()
D.getinfo()
M.getinfo()
SM.getinfo()
