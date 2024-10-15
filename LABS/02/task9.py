with open("newfile.txt") as file:
    a = file.read()
    
charcount = len(a)

wordcount = len(a.split())

print(charcount)
