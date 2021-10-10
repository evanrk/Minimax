from Decision_tree2 import minimax


bot = "X"
player = "O"

board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}

def print_board(board):
    print("""
    {board[1]} | {board[2]} | {board[3]}
    -+-+-+-+-
    {board[4]} | {board[5]} | {board[6]}
    -+-+-+-+-
    {board[7]} | {board[8]} | {board[9]}
    """.format(board = board))

print_board(board)

def is_space_free(space):
    if board[space] == " ":
        return True
    else:
        return False

def is_win():
    #checks every way that the anyone can win
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False
    
def check_winner(sign):
    if (board[1] == board[2] and board[1] == board[3] and board[1] != sign):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != sign):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != sign):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != sign):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != sign):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != sign):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != sign):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != sign):
        return True
    else:
        return False

def is_draw():
    for i in board.keys():
        if i == " ":
            return False
    
    #else:
    return True


def insert_sign(space, sign):
    if is_space_free(space):
        board[space] = sign
        if is_draw():
            print("Draw!")
        elif is_win():
            if sign == "X":
                print("Bot Wins!")
            else:
                print("Player Wins!")

alpha = 0.3
def minmax():
    
    if check_winner(bot):
        return 100 * alpha
    elif check_winner(player):
        return -100 * alpha
    elif is_draw():
        return 0
    
    for i in board.keys():
        if board[i] == " ":
            board[i] = bot
            minimax
    
    