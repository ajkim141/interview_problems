# Alex Kim - Minesweeper

import random

# Initial board setup

r1 = ["X","X","X","X","X","X","X"]
r2 = ["X","X","X","X","X","X","X"]
r3 = ["X","X","X","X","X","X","X"]
r4 = ["X","X","X","X","X","X","X"]
r5 = ["X","X","X","X","X","X","X"]
r6 = ["X","X","X","X","X","X","X"]
r7 = ["X","X","X","X","X","X","X"]

game_board = [r1, r2, r3, r4, r5, r6, r7]

# Draw the board

def draw_grid(board):
    print ("    1    2    3    4    5    6    7")
    print 1 , board[0]
    print 2 , board[1]
    print 3 , board[2]
    print 4 , board[3]
    print 5 , board[4]
    print 6 , board[5]
    print 7 , board[6]

# Randomize mines
def random_mines(board):
    board[0] = [(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1))]
    board[1] = [(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1))]
    board[2] = [(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1))]
    board[3] = [(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1))]
    board[4] = [(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1))]
    board[5] = [(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1))]
    board[6] = [(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1)),(False, random.randint(0, 1))]

    game_board = [board[0], board[1], board[2], board[3], board[4], board[5], board[6]]

    return game_board

