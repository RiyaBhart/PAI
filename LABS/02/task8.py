
x = int(input("Choose the currency you want to convert from: \n1. Euro\n2. Dollar\n3. PKR\n4. INR\n5. Yen\n"))
y = int(input("Enter Amount: "))
z = int(input("Choose the currency you want to convert to: \n1. Euro\n2. Dollar\n3. PKR\n4. INR\n5. Yen\n"))

if x == z:
    print("The amount is already in the given currency.")
else:
    if x == 1:  # Euro
        if z == 2:
            amount = y * 1.0788
            print("Amount in Dollars is:", amount)
        elif z == 3:
            amount = y * 308.01
            print("Amount in PKR is:", amount)
        elif z == 4:
            amount = y * 92.65
            print("Amount in INR is:", amount)
        elif z == 5:
            amount = y * 161.46
            print("Amount in Yen is:", amount)

    elif x == 2:  # Dollar
        if z == 1:
            amount = y / 1.0788
            print("Amount in Euro is:", amount)
        elif z == 3:
            amount = y * (308.01 / 1.0788)
            print("Amount in PKR is:", amount)
        elif z == 4:
            amount = y * (92.65 / 1.0788)
            print("Amount in INR is:", amount)
        elif z == 5:
            amount = y * (161.46 / 1.0788)
            print("Amount in Yen is:", amount)

    elif x == 3:  # PKR
        if z == 1:
            amount = y / 308.01
            print("Amount in Euro is:", amount)
        elif z == 2:
            amount = y / (308.01 / 1.0788)
            print("Amount in Dollars is:", amount)
        elif z == 4:
            amount = y * (92.65 / 308.01)
            print("Amount in INR is:", amount)
        elif z == 5:
            amount = y * (161.46 / 308.01)
            print("Amount in Yen is:", amount)

    elif x == 4:  # INR
        if z == 1:
            amount = y / 92.65
            print("Amount in Euro is:", amount)
        elif z == 2:
            amount = y / (92.65 / 1.0788)
            print("Amount in Dollars is:", amount)
        elif z == 3:
            amount = y * (308.01 / 92.65)
            print("Amount in PKR is:", amount)
        elif z == 5:
            amount = y * (161.46 / 92.65)
            print("Amount in Yen is:", amount)

    elif x == 5:  # Yen
        if z == 1:
            amount = y / 161.46
            print("Amount in Euro is:", amount)
        elif z == 2:
            amount = y / (161.46 / 1.0788)
            print("Amount in Dollars is:", amount)
        elif z == 3:
            amount = y * (308.01 / 161.46)
            print("Amount in PKR is:", amount)
        elif z == 4:
            amount = y * (92.65 / 161.46)
            print("Amount in INR is:", amount)
