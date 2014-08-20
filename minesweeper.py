# Alex Kim - Minesweeper

import random

# Initial board setup

r1 = ["O","O","O","O","O","O","O"]
r2 = ["O","O","O","O","O","O","O"]
r3 = ["O","O","O","O","O","O","O"]
r4 = ["O","O","O","O","O","O","O"]
r5 = ["O","O","O","O","O","O","O"]
r6 = ["O","O","O","O","O","O","O"]
r7 = ["O","O","O","O","O","O","O"]

game_board = [r1, r2, r3, r4, r5, r6, r7]

# Draw the board

def draw_grid(board):
    #print ("    1    2    3    4    5    6    7")
    interpret_row(board[0])
    interpret_row(board[1])
    interpret_row(board[2])
    interpret_row(board[3])
    interpret_row(board[4])
    interpret_row(board[5])
    interpret_row(board[6])

# Randomize mines
# False: space has not been revealed
# True: space has been revealed
# 0: empty
# 1: mine
def random_mines(board):
    board[0] = [(False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1))]
    board[1] = [(False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1))]
    board[2] = [(False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1))]
    board[3] = [(False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1))]
    board[4] = [(False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1))]
    board[5] = [(False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1))]
    board[6] = [(False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1)), (False, random.randint(0, 1))]

    game_board = [board[0], board[1], board[2], board[3], board[4], board[5], board[6]]

    return game_board

# Handle hiding and revealing spaces
def interpret_row(row):
    for i in row:
        if not i[0]:
            print "[O]", "\r"
        else:
            if i[-1] == 0:
                print "[ ]", "\r"
            else:
                print "[X]", "\r"

