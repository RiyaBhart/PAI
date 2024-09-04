list1 = input("Enter the first list elements : ").split()
list2 = input("Enter the second list elements : ").split()

if len(list1) != len(list2):
    print("Error: The lists must have the same number of elements.")
else:
    dictionary = {}
    for i in range(len(list1)):
        dictionary[list1[i]] = list2[i]
    print(dictionary)
