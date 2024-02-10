choice = ["g", "y", "b"]

print("Enter 'g' for green, 'y' for yellow, and 'b' for brown.")
condition = input("Enter your choice(g, y, b): ").lower()
if condition in choice:
    if condition == "g":
        print("Unripe")
    elif condition == "y":
        print("Ripe")
    else:
        print("Overripe")
else:
    print("Invalid choice.")
