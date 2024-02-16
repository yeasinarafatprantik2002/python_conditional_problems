number = input("Enter a number: ")
number = int(number) if number.isdigit() else float(number)

if number.is_integer() or float(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")
else:
    print("Invalid input")
