weathers = ["sunny", "rainy", "snowy"]

choice = input("Enter the weather(sunny, rainy, snowy): ").lower()

if choice in weathers:
    if choice == "sunny":
        print("Go for a walk.")
    elif choice == "rainy":
        print("Read a book.")
    else:
        print("Build a snowman.")
else:
    print("Invalid choice.")
