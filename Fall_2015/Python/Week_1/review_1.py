def main():
    
    """
    This is a review of what we went over in the
    first class for Beginning Python.
    
    Things covered:
    Print statements
    Comments, multi-line comments
    variables, variable types
    Prompting user
    Taking user input
    """

    print("This is my review for class session 1.")

    # Below we will list all the different
    # types of variables

    c = "c"             # char
    i = 100             # int
    f = 3.14            # float
    s = "This is my string variable" # string

    print(c)
    print(i)
    print(f)
    print(s)

    name = input("Please input your name")

    print("Your name is, " + name)

if __name__ == "__main__":
    main()
