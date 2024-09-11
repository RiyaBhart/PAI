class Employee:
    def get_data(self):
        self.name = input("Enter name: ")
        self.salary = float(input("Enter salary: "))
        self.taxp = float(input("Enter percentage of tax: "))

    def salary_after_tax(self):
        tax_amount = (self.taxp / 100) * self.salary
        salary_after_tax = self.salary - tax_amount
        return salary_after_tax

    def update_tax_percentage(self):
        self.taxp = float(input("Enter updated tax percentage: "))
        return self.taxp

a = Employee()

a.get_data()

print(f"Salary after tax: {a.salary_after_tax()}")

print(f"Updated tax percentage: {a.update_tax_percentage()}")
