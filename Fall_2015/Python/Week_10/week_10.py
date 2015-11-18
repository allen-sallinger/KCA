# week_10.py
# In this program we will use the week_5.py file as a template.
# We will then create an "AI" that the computer can play against.

import random

def check_win(game_board, game_over):
    # check if a vertical win
    if(game_board[0][0] != ". " and game_board[0][0] == game_board[1][0] and game_board[0][0] == game_board[2][0]):
        game_over = 1
        return game_over
    
    if(game_board[0][1] != ". " and game_board[0][1] == game_board[1][1] and game_board[0][1] == game_board[2][1]):
        game_over = 1
        return game_over

    if(game_board[0][2] != ". " and game_board[0][2] == game_board[1][2] and game_board[0][2] == game_board[2][2]):
        game_over = 1
        return game_over

    # check if horizontal win
    if(game_board[0][0] != ". " and game_board[0][0] == game_board[0][1] and game_board[0][0] == game_board[0][2]):
        game_over = 1
        return game_over

    if(game_board[1][0] != ". " and game_board[1][0] == game_board[1][1] and game_board[1][0] == game_board[1][2]):
        game_over = 1
        return game_over

    if(game_board[2][0] != ". " and game_board[2][0] == game_board[2][1] and game_board[2][0] == game_board[2][2]):
        game_over = 1
        return game_over

    # check TL -> BR win
    if(game_board[0][0] != ". " and game_board[0][0] == game_board[1][1] and game_board[0][0] == game_board[2][2]):
        game_over = 1
        return game_over

    # check BL->TR
    if(game_board[2][0] != ". " and game_board[2][0] == game_board[1][1] and game_board[2][0] == game_board[0][2]):
        game_over = 1
        return game_over

    else:
        return 0
    

def ai_move(game_board, piece):
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

        game_over = check_win(game_board, game_over)
        if(game_over == 1):
            print("Player won")
            break

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

        # Ends game if there is a win
        game_over = check_win(game_board, game_over)
        if(game_over == 1):
            print("AI won")
            break

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
