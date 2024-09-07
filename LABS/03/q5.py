try: 
    import json

    list1=input("Enter names of people : ").split()
    list2=input("enter age of people : ").split()

    if(len(list1)!=len(list2)):
        print("Error, lengths are different")
    else:
        dictionary={}
        for i in range(len(list1)):
            dictionary[list1[i]]=list2[i]
        print(dictionary)
        with open('q5.txt','w') as file:
            file.write(str(dictionary))
        
except Exception as e:
    print("An error occured ",e)
