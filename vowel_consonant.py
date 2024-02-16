letter = input("Enter a letter: ").lower()

if letter.isalpha():
    if letter in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")
