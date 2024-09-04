try:
    with open('task2.txt', 'r') as file:
        a=file.read()
        b= a.replace('cat','food')

    print(b)

except FileNotFoundError:
    print("File Not Found")
