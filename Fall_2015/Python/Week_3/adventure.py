# adventure.py
# A text based adventure game
# Author: Allen Sallinger
# Date: 9/30/15

def main():

    # Get the adventurers name
    name = input("What is your name wise adventurer?")

    # Greet the adventurer
    print("You may last for many years or many seconds " + name)
    print("Choose your path wisely.")

    # First step
    print("You come to a fork in the road.")
    print("The left path takes you into a forrest.")
    print("The right path takes you into a cave deep in the mountain")

    user_choice = input("Enter A: to go left or B: to go right")

    if(user_choice.lower() == "a"):
        print("You have now entered the forrest. There is an owl in a tree")
        print("The owl offers you a weapon of choice.")

        user_choice = input("Enter A: for sword, B: for rock, or C: for wand")

        if(user_choice.lower() == "a"):
            print("You got a sword")

        if(user_choice.lower() == "b"):
            print("You got a rock")

        else:
            print("You got a wand")

    else:
        print("You have now entered the cave. There is a rock golumn")
        print("The golumn offered you a weapon of your choice")
        user_choice = input("Enter A: for sword, B: for rock, or C: for wand")

        if(user_choice.lower() == "a"):
            print("You got a sword")

        if(user_choice.lower() == "b"):
            print("You got a rock")

        else:
            print("You got a wand")


main()
