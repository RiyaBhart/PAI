def userfeedback():
    name = input("Your good name: ")
    print(f"Hello! {name}")
    print("I hope you are fine, let me know how I can help you!")

    response = input("Do you need help? (yes/no): ").strip().lower()

    if response == 'yes':
        problem = input("Share your problem with us: ")
        print("Thanks for your feedback, we will resolve your problem.")
    else:
        print(f"{'Okay! Good to see you, stay connected'.center(44)}")


userfeedback()
