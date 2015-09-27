def main():
    # Learned how to print
    #print("Good morning")

    # Define a variable greeting
    #greeting = "Good Afternoon"

    # A way to print using variables.
    #print(greeting)

    name = input("Please tell us your name: ")

    print("Hello, " + name)

    # Simple survey
    # What is their favorite color
    # What is their hobby / like
    # Favorite Animal

    color = input("What is your favorite color: ")

    hobby = input("What is your favorite hobby: ")

    animal = input("What is your favorite animal: ")

    print("Favorite Color: " + color)
    print("Favorite Hobby: " + hobby)
    print("Favorite Animal: " + animal)
    
    # Create first control statement
    if(color == "Blue"):
        print("Both our favorite colors are Blue")

    else:
        print("We have different favorite colors")

main()
