number1 = input("Enter First number: ")
number2 = input("Enter Second number: ")
number3 = input("Enter Third number: ")
largest = 0

if number1.isdigit() and number2.isdigit() and number3.isdigit():
    if number1 > number2 and number1 > number3:
        largest = number1
        print(f"{number1} is the largest number")
    elif number2 > number1 and number2 > number3:
        largest = number2
        print(f"{number2} is the largest number")
    elif number3 > number1 and number3 > number2:
        largest = number3
        print(f"{number3} is the largest number")
    else:
        largest = number1
        print("The numbers are equal")
else:
    print("Invalid input")

num = largest

if num.isdigit():
    num = int(num)
    if num % 2 == 0 and num != 0:
        print("Even")
    elif num == 0:
        print("Zero")
    else:
        print("Odd")

else:
    print("Invalid input")
