import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    # Specify the range
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))

    # Generate a random number within the specified range
    target_number = random.randint(lower_bound, upper_bound)

    # Initialize variables
    guess = None
    attempts = 0

    print(f"Guess a number between {lower_bound} and {upper_bound}")

    # Game loop
    while guess != target_number:
        # Get the user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Provide feedback
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts.")


# Run the game
number_guessing_game()
