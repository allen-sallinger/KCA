# nested.py
# This example shows how control statements can
# be nested to create more complex control flows


def main():

    # take user input to choose path a or  b
    choice = input("Choose path a or path b: ")

    if(choice.lower() == "a"):
        print("You chose path a")
        choice = input("Choose a secondary path, either path 1 or path 2")

        # these are nested if statements
        if(choice == 1):
            print("You chose path 1 and the dragon ate you")


        if(choice == 2):
            print("You chose path 2 and made it to the castle")

        else:
            print("You did not choose a path and a troll ate you.")

    if(choice.lower() == "b"):
        print("You chose path b")

        choice = input("Do you go down path 1 or path 2")

        if(choice == 1):
            print("You went on path 1 and got to ride in a boat, cool!")

        if(choice == 2):
            print("You got eaten by a sea serpent on this path")

        else:
            print("You got to a beach and safely made a sand castle")

main()
