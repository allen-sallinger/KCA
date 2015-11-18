# week_10.py
# In this program we will use the week_5.py file as a template.
# We will then create an "AI" that the computer can play against.

import random

def ai_move(game_board, piece):
    #if(piece == "x "):
#        piece == "o "

#    else:
#        piece == "x "
    piece = "o "
        
    x = random.randint(0,2)
    y = random.randint(0,2)

    while(game_board[x][y] != ". "):
        x = random.randint(0,2)
        y = random.randint(0,2)

    game_board[x][y] = piece

    return game_board
    

def main():

    game_board = []

    # Create the game_board
    for i in range(3):
        game_board.append([])
        for j in range(3):
            row =". "
            game_board[i].append(row)

    # Print out the game_board
    print("Starting tic-tac-toe!!!")
    for row in game_board:
        t_row = ""
        for col in row:
            t_row = t_row + col
        print(t_row)

    piece = "x "

    game_over = 0

    while(game_over != 1):
        c_row = int(input("Please input a row"))
        c_col = int(input("Please input a col"))

        piece = "x "
        if(game_board[c_row][c_col] == ". "):
            game_board[c_row][c_col] = piece

#            if(piece == "x "):
#                piece = "o "
#            else:
#                piece = "x "

        game_over = 1
        for i in range(3):
            for j in range(3):
                if(game_board[i][j] == ". "):
                    game_over = 0
                    break

        print("Player's turn")
        for row in game_board:
            t_row = ""
            for col in row:
                t_row = t_row + col
            print(t_row)

        game_board = ai_move(game_board, piece)

        print("AIs turn: ")
        for row in game_board:
            t_row = ""
            for col in row:
                t_row = t_row + col
            print(t_row)

        game_over = 1
        for i in range(3):
            for j in range(3):
                if(game_board[i][j] == ". "):
                    game_over = 0
                    break






                

    print("The game is over")

    for row in game_board:
            t_row = ""
            for col in row:
                t_row = t_row + col
            print(t_row)
    
main()
