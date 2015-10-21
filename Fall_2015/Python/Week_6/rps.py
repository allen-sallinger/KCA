# rps.py
# A simple game of rock, paper, scissors.

import random

def get_rand():
    rand = random.randint(0,2)
    return rand

def get_input():
    user_input = int(input("Guess 0 for rock, 1 for paper, and 2 for scissors"))
    return user_input

def main():
    print("Welcome to Rock Paper Scissors")
    rand = get_rand()
    user_input = get_input()

    if(user_input == rand):
        print("You tied")

    if(user_input == 0 and rand == 1):
        print("You lost by paper")

    if(user_input == 1 and rand == 2):
        print("You lost by scissors")

    if(user_input == 2 and rand == 0):
        print("You lost by rock")

    if(user_input == 0 and rand == 2):
        print("You won with rock")

    if(user_input == 1 and rand == 0):
        print("You won with paper")

    if(user_input == 2 and rand == 1):
        print("You won with scissors")


main()
