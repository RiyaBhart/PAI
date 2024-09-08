try:
        
    with open("q7.txt", "r") as file:
        content = file.read()

    print("Original content:", content)
       
    correctedcontent = ""
    for char in content:
        if char == 'm':
            correctedcontent += 's'
        else:
            correctedcontent += char

       
    with open("q7.txt", "w") as file:
        file.write(correctedcontent)

    print("Corrected content:", correctedcontent)

except FileNotFoundError:
    print("Error: The file 'q7.txt' was not found.")
except IOError:
    print("Error: An issue occurred while reading or writing to the file.")
except Exception as e:
    print("An unexpected error occurred: ",e)

