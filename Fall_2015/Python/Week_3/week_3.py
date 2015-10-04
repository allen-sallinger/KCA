# week_3.py
# Author: Allen Sallinger
# Date: 9/30/15

def main():

    # Overview of past week and this weeks mission/idea
    """
    Last week we covered if/else statements along with a short intro
    on arrays and for loops. This week we will continue on arrays and
    the methods associated with them and how to use our new control
    statements, loops.
    """

    # How to make an array and what can arrays hold
    array_ints = [1,2,42]
    array_floats = [3.14, 6.28, 2.7]
    array_strings = ["life", "universe", "everything"]

    # How to print out the whole array?
    print("I am printing out the arrays as a whole")
    print(array_ints)
    print(array_floats)
    print(array_strings)

    # How to print out the contents of an array
    print("I am printing out the contents of the arrays")

    # Ways to print out the contents of an array



    # For info on control elements go to this link:
    # https://docs.python.org/3.5/tutorial/controlflow.html
    # For elements in an array
    for i in array_ints:
        print(i)

    # For elements in range of arrays size
    for i in range(len(array_strings)):
        print(i)

    # At this point in class we transitioned to creating into creating
    # an adeventure game. It is in the file adventure.py


main()



