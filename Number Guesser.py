import random
def number_guesser():
    print("Welcome to the Number Guesser Game!")
    try:
        lower = int(input("Enter the lower bound of the range: "))
        upper = int(input("Enter the upper bound of the range: "))
        if lower >= upper:
            print("Upper bound must be greater than lower bound.")
            return
        number_to_guess = random.randint(lower, upper)
        attempts = 0
        print(f"\nI'm thinking of a number between {lower} and {upper}. Try to guess it!")
        while True:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"You got it! The number was {number_to_guess}.")
                print(f"Total attempts: {attempts}")
                break
    except ValueError:
        print("Please enter valid numbers only.")
# Start the game
number_guesser()
