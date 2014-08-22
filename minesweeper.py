# Alex Kim - Minesweeper

import random

# Initial setup

game_board = list()
game_on = True

# Draw the board
def draw_grid(board):
    print ("   1   2   3   4   5   6   7")
    row_num = 1
    for i in board:
        print row_num,
        row_num += 1
        interpret_row(i)
        print "\n"

# Randomize mines
# False: space has not been revealed
# True: space has been revealed
# 0: empty
# 1: mine
def random_mines(board):
    for i in xrange(7):
        board.append([[False, random.randint(0, 1)], [False, random.randint(0, 1)], [False, random.randint(0, 1)], [False, random.randint(0, 1)], [False, random.randint(0, 1)], [False, random.randint(0, 1)], [False, random.randint(0, 1)]])

    return board

# Handle hiding and revealing spaces
def interpret_row(row):
    for i in row:
        if not i[0]:
            print"[O]",
        else:
            if i[-1] == 0:
                print"[ ]",
            else:
                print"[X]",


# Handle player input
def click_space(game_board):
    print "Enter Row"
    mine_x = input() - 1

    while mine_x > len(game_board) - 1:
        print "Too Large, Try Again"
        mine_x = input() - 1

    print "Enter Column"
    mine_y = input() - 1

    while mine_y > len(game_board[mine_x]) - 1:
        print "Too Large, Try Again"
        mine_y = input() - 1

    game_board[mine_x][mine_y][0] = True

# Game over
def game_over(game_board):
    for i in game_board:
        for j in i:
            if j[-1] == 1:
                j[0] = True

    print "Game Over"
    draw_grid(game_board)
    game_on = False


'''
# Output test
draw_grid(random_mines(game_board))
'''

# Game test
print "Minesweeper"

while True:
    draw_grid(random_mines(game_board))


    while game_on:
        click_space(game_board)
        draw_grid(game_board)

    break