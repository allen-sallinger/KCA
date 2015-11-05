# week_8.py
# This code is a modified version of week 7. In it we take user input
# to allow the user to move their character 'x' around the board.



import random
def take_input():
    print("Enter w for up, a for left, d for right, s for down")
    move = input()
    move = move.lower()
    while(True):
        if(move == 'w'):
            return move
        if(move == 'd'):
            return move
        if(move == 'a'):
            return move
        if(move == 's'):
            return move
        else:
            return take_input()

    return move

#  Create function  to take the move and move the character
def move_piece(board, move, cpos):
    x = cpos[0]
    y = cpos[1]
    board[x][y] = ". "
    if(move == 'a' and x > 0):
        cpos = [x, y - 1]

    elif(move == 'w' and y > 0):
        cpos = [x - 1, y]

    elif(move == 'd' and x < 9):
        cpos = [x, y + 1]

    elif(move == 's' and y < 9):
        cpos = [x + 1, y]

    board[x][y] = "x "

    return (board, cpos)

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
    return (board, [x,y])
    
def place_character(board):
    x = random.randint(0,9)
    y = random.randint(0,9)

    board[x][y] = "x "
    return (board,[x,y])

def main():

    print("Entered the game")
    board = generate_board()

    print("Placing the flag \n\n\n")

    board_flag = place_flag(board)
    board = board_flag[0]
    fpos = board_flag[1]
    print_board(board)

    print("Placing the character \n\n")
    board_char = place_character(board)
    board = board_char[0]
    cpos = board_char[1]
    print_board(board)

    while(cpos != fpos):
        #Get aswd input from the user
        move = take_input()
        board_move = move_piece(board, move, cpos)
        board = board_move[0]
        cpos = board_move[1]
        print_board(board)
        
    print("You won the game")
    print("The game has terminated")

    #end of main function


main()
