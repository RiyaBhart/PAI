print("Enter two integers to divide.")

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ValueError:
    print("Invalid input. Please enter integers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("The result of ",numerator," divided by ",denominator ," is ",result)
