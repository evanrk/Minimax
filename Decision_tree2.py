"""
Author: Evan Klein
My first attempt at improving the minimax code:
I tried to improve the decision tree by weighting the wins/losses by how far down they are in the decision tree and then add them up to come up with a total score for each move.
"""

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

def is_space_free(position):
    if board[position] == " ":
        return True
    else:
        return False

def check_draw():
    for key in board.keys():
        if board[key] == " ":
            return False
    return True

def check_win():
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

def check_winner(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] != mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != mark):
        return True
    else:
        return False

def insert_letter(letter, position):
    if is_space_free(position):
        board[position] = letter
        print_board(board)
        if check_draw():
            print("Draw!")
            exit()
        
        if check_win():
            if letter == "X":
                print("Bot Wins!")
                exit()
            else:
                print("Player Wins!")
                exit()

    else:
        print("can't insert there")
        position = int(input("Enter new position: "))
        insert_letter(letter, position)

#ignore depth, tic tac toe is not complicated enough for it

alpha = 0.7

def minimax(board, depth, is_maximizing, iters):
    if check_winner(bot):
        return 100 * alpha ** iters
    elif check_winner(player):
        return -100 * alpha ** iters
    elif check_draw():
        return 0

    if is_maximizing:
        if board[key] == " ":
            board[key]


def minimax(board, depth, is_maximizing, iterations):
    if check_winner(bot):
        return 100 * alpha ** iterations
    elif check_winner(player):
        return -100 * alpha ** iterations
    elif check_draw():
        return 0
    if is_maximizing:
        best_score = -1000

        for key in board.keys():
            if board[key] == " ":
                board[key] = bot
                score = minimax(board, 0, False, iterations + 1)
                board[key] = " "
                if score > best_score:
                    best_score = score
        
        return best_score

    else:
        best_score = 800

        for key in board.keys():
            if board[key] == " ":
                board[key] = bot
                score = minimax(board, depth, True, iterations + 1)
                board[key] = " "
                if score < best_score:
                    best_score = score
    return best_score


player = "O"
bot = "X"
def player_move():
    position = int(input("Enter the position for O: "))
    insert_letter(player, position)
    return

def com_move():
    best_score = -1000
    best_move = 0

    for key in board.keys():
        if board[key] == " ":
            board[key] = bot
            score = minimax(board, 0, False, 0)
            board[key] = " "
            if score > best_score:
                best_score = score
                best_move = key
    
    insert_letter(bot, best_move)
    return

print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")

while not check_win():
    com_move()
    player_move()