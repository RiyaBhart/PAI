with open('task1.txt', 'r') as file:
    a = file.read()
    a = a.replace(' ', '')
    charcount = len(a)
print(charcount)
