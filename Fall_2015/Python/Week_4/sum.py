# sum.py
# this program calculates the sum of the numbers from 1 - 5
# Week_4 project program

def main():
    sum = 0
    arr = [1,2,3,4,5]

    # Way 1 to compute sum
    print("Using for loop to compute the sum")
    for num in arr:
        sum = sum + num
    print(sum)

    # Way 2 to compute sum
    sum = 0
    counter = 0
    print("Using while loop to compute the sum")
    while counter < len(arr):
        sum = sum + arr[counter]
        counter = counter + 1
    print(sum)


main()
