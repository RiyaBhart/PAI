
userurl = input("Enter your URL (it should start with http://www.): ")


if userurl.startswith("http://www."):
    
    newurl = userurl.replace("http://www.", "") + ".com"
    print("Converted URL:", newurl)
else:
    print("The URL must start with http://www.")
