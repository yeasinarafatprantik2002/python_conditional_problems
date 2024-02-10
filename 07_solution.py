order_choice = ["small", "medium", "large"]

extra_shot = True if input("Do you want an extra shot(y/n)? ").lower() == "y" else False

size = input("Enter the size(small, medium, large): ").lower()

if extra_shot and size in order_choice:
    print(f"{size} coffee with an extra shot is added.")
elif size in order_choice:
    print(f"{size} coffee is added.")
else:
    print("Invalid choice.")
