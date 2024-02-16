num = input("Enter a number: ")

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


# num = input("Enter a number: ")

# try:
#     num = int(num)
#     if num % 2 == 0 and num != 0:
#         print("Even")
#     elif num == 0:
#         print("Zero")
#     else:
#         print("Odd")
# except ValueError:
#     print("Invalid input")
