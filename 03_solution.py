score = int(input("Enter your score: "))
if score >= 101:
    print("Invalid score.")
else:
    grade = (
        "A"
        if score >= 90
        else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
    )
    print(f"Your grade is {grade}.")
