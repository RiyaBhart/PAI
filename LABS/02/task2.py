def checklastletter(givenstring):
    vowels = 'aeiouAEIOU'
    
    

    lastletter = givenstring[-1]


    if lastletter in vowels:
        return "The last letter is a vowel."
    else:
        return "The last character is a consonant."


givenstring = input("Enter a string: ")
print(checklastletter(givenstring))
