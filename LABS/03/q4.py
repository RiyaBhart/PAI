try:

    name = input("Enter name: ")
    cnic = int(input("Enter CNIC: "))
    age = int(input("Enter age: "))
    salary = int(input("Enter salary: "))


    with open('task4.txt', 'w') as file:
        file.write(f"Name: {name}\nCNIC: {cnic}\nAge: {age}\nSalary: {salary}\n")

    contact = int(input("Enter contact number: "))


    with open('task4.txt', 'a') as file2:
        file2.write(f"Contact Number: {contact}\n")


    with open('task4.txt', 'r') as file3:
        content = file3.read()
        print(content)

except ValueError:
    print("Invalid input. Please enter the correct data type.")
except FileNotFoundError:
    print("File not found.")
