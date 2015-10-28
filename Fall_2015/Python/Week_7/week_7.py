# week_7.py
# Making a game where you are a character and you must reach the flag.
# Play on a game created in CS 112 at SCC with Graham Smallwood
# Author: Allen Sallinger

#def take_input():
#    return input("Type a for up, s for down, ")

import random

def print_board(board):
    for row in board:
        t_row = ""
        for col in row:
            t_row = t_row + col
        print(t_row)
    
def generate_board():
    board = []
    for i in range(10):
        board.append([])
        for j in range(10):
            row = ". "
            board[i].append(row)

    print_board(board)

    return board

def place_flag(board):
    x = random.randint(0,9)
    y = random.randint(0,9)

    board[x][y] = "F "
    return board
    
def place_character(board):
    x = random.randint(0,9)
    y = random.randint(0,9)

    board[x][y] = "x "
    return board

def main():

    print("Entered the game")
    board = generate_board()

    print("Placing the flag \n\n\n")

    board = place_flag(board)
    print_board(board)

    print("Placing the character \n\n")
    board = place_character(board)
    print_board(board)

    print("The game has terminated")
    






main()
