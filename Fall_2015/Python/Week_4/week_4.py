# week_4.py
# This week we will be going forward with control structures.
# We will cover for loops and while loops.
# Go over nested functions

def main():

    arr = [1,2,3,4,5]
    # For loop Example
    for num in arr:
        print(num)

    
    # While loop Example
    arr = ["a","b","c","d","e"]
    counter = 0
    print("This is a while loop running")
    while counter < len(arr):
        print(arr[counter])
        counter = counter + 1

    # Point of this?
    # The control flows are different but can generate the same results

main()
