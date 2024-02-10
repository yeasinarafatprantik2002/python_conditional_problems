distance = int(input("Enter the distance in km: "))

if distance < 3:
    print("You can walk.")
elif distance < 15:
    print("You can take a bike.")
else:
    print("You can take a car.")
