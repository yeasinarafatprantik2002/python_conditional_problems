choice = "mf"
char = input("Enter a letter: ").lower()

if char.isalpha():
    if len(char) == 1:
        if char in choice:
            if char == "m":
                print("Male")
            else:
                print("Female")
        else:
            print("Invalid input")
    else:
        print("Invalid input")
else:
    print("Invalid input")
