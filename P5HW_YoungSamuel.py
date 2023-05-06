# Math Quiz Generator
# 5-5-23
# CTI-110 P5HW - Math Quiz   
# Young, Samuel
#


import random

def adding_quiz():
    # Generate two random numbers
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    # Display the addition problem
    print(f"  {num1}\n+ {num2}\n")
    answer = num1 + num2

    # Prompt the user to enter their guess
    guess = int(input("Enter answer.\n"))

    # Loop until the user guesses correctly
    num_guesses = 1
    while guess != answer:
        if guess < answer:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")
            print()
        guess = int(input("Try again: "))
        num_guesses += 1

    # Congratulate the user on a correct guess and show the number of guesses
    print("Congratulations!!!! Your answer is correct.")
    print(f"Number of guesses: {num_guesses}")
    print()

# Display the main menu and get the user's choice
print("Welcome to Math Quiz\n")
while True:
    print("MAIN MENU")
    print("----------------------------------------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit\n")
    choice = int(input("Please choose one of the menu options: "))

    # Call the appropriate function based on the user's choice
    if choice == 1:
        adding_quiz()
    elif choice == 2:
        # Implement the subtraction quiz function here
        pass
    elif choice == 3:
        print("Thank you for playing...\nBye!!")
        break
    else:
        print("Invalid choice. Please try again.\n")
