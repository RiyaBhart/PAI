def build_message(**info):
    message = ""
    for key, value in info.items():
        message += key + ": " + str(value) + "\n"
    return message


result = build_message(name="Riya", age=18, city="Karachi")
print(result)
