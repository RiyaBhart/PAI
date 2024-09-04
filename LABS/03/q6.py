def main():
    textinput = input("Enter a sentence: ").strip()

    if textinput.endswith('?'):
        try:
            with open('questions.txt', 'a') as file:
                file.write(textinput + '\n')
                print("Question has been written to file")
        except FileNotFoundError:
            print("File doesn't exist in system")
    else:
        print("The sentence is not a question. Nothing was written to the file.")

main()
