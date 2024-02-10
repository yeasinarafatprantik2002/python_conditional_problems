pet = ["dog", "cat"]

choice = input("Enter a pet(dog, cat): ")
age = int(input("Enter the age of the pet: "))
if choice in pet:
    if choice == "dog" and age < 2:
        print("Puppy food")
    elif choice == "dog" and age >= 2:
        print("Adult dog food")

    else:
        if choice == "cat" and age > 5:
            print("Senior cat food")
        else:
            print("Kitten food")
