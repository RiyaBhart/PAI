def employee(name, salary=60000):
    tax = salary * 0.02
    salaryaftertax = salary - tax
    print("Employee: ",name)
    print("Salary after tax: $",salaryaftertax)

employee("ABC", 90000)
employee("Ali")