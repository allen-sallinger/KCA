# guess.py
# This program asks the user to guess a random number that is generated.

import random

# Get a random number between 0 and 4
def generate_random():
    num = random.randint(0,4)
    return num

# Takes the users input
def get_guess():
    guess = int(input("Please guess a number between 0 and 4"))
    return guess

def main():
    guess = get_guess()
    num = generate_random()

    # Take guesses until user is correct
    while(num != guess):
        print("You guessed wrong. Guess Again")
        guess = get_guess()


    print("You guessed correctly. The number was: ")
    print(num)


main()
