import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    # Loop until the correct number is guessed
    while not guessed:
        try:
            # Take input from the user
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Provide feedback to the user
            if user_guess < number_to_guess:
                print("Too low!")
            elif user_guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 100.")

# Run the game
guessing_game()
