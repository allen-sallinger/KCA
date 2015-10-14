# week_5.py
# In this program we are going to create the basis for our game board
# which we will use across multiple games that we will create for the rest
# of the semester.

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

        if(game_board[c_row][c_col] == ". "):
            game_board[c_row][c_col] = piece

            if(piece == "x "):
                piece = "o "
            else:
                piece = "x "

        game_over = 1
        for i in range(3):
            for j in range(3):
                if(game_board[i][j] == ". "):
                    game_over = 0

        for row in game_board:
            t_row = ""
            for col in row:
                t_row = t_row + col
            print(t_row)

    print("The game is over")
    
main()
