# Alex Kim - Minesweeper

import random

# Initial board setup


# for these, you can instead do ["O"] * 7 to get the same result. However, you should never hardcode something like
# this. It would be much better to create the board from the list of states
# r1 = ["O","O","O","O","O","O","O"]
# r2 = ["O","O","O","O","O","O","O"]
# r3 = ["O","O","O","O","O","O","O"]
# r4 = ["O","O","O","O","O","O","O"]
# r5 = ["O","O","O","O","O","O","O"]
# r6 = ["O","O","O","O","O","O","O"]
# r7 = ["O","O","O","O","O","O","O"]

# given that pretty much every function needs access to game_board, why not make is a global? That being said,
# it's better practice to avoid globals like the plauge
# game_board = [r1, r2, r3, r4, r5, r6, r7]
# game_on = True


# Draw the board
# def draw_grid(board):
def render_board(game_board):
    # let's try to aim for something more like this:
    #   0 1 2 3 4 5 6
    #  +-------------+
    # 0|O O O O O O O|
    # 1|O O O O O O O|
    # 2|O O O O O O O|
    # 3|O O O O O O O|
    # 4|O O O O O O O|
    # 5|O O O O O O O|
    # 6|O O O O O O O|
    #  +-------------+

    # get the dimensions
    height = len(game_board)
    width = len(game_board[0])

    # add some white space
    print ""

    # instead of hardcoding it, you can use the join function instead (added perk that this is flexible
    # over varying lengths of boards)
    # print ("   1   2   3   4   5   6   7")
    header_row = [str(i) for i in range(width)]
    print "  " + " ".join(header_row)
    boarder_row = [" +"] + (["-"] * (width * 2 - 1)) + ["+"]
    print "".join(boarder_row)

    # there's a handy function called enumerate() that takes something that you can loop iterate (loop) through and
    # returns to you a tuple of ('what loop number am I currently on", "value of element")

    #rn = 1
    for rn, row in enumerate(game_board):
        # print rn, <-- why are you putting comma's at the end of things?

        # let's make a list of the row's elements, along with it's boarders, to then join & print
        row_value = str(rn) + "|" + " ".join([render_tile(tile) for tile in row]) + "|"
        print row_value
    # print "\n" printing \n will only work on unix, in windows its \r\n (stands for carriage return, new line)
    print "".join(boarder_row)
    print ""


# good job with the documentation, but it should go in the function itself, specifcially in the docstring
# Randomize mines
# False: space has not been revealed
# True: space has been revealed
# 0: empty
# 1: mine
# def random_mines(game_board):
#     # Again with the hardcoding, don't do this. Programmers are meant to be lazy in a good way. If you find yourself
#     # hardcoding something like this (that's repetitive) you're probably doing something wrong (computers are good at
#     # repetitive things, use them for it.
#     # e.g.
#     # foo = list()
#     # for i in range(ten):
#     #   foo[i] = [some list you make)
#
#     # also, this line extends too far to the right (the PEP8 limit is 120 which pycharm should be forcing you towards
#     # (thats what the yellow underlines are for). If you must go over the limit, use "\" to signify a line continuation:
#     # board[0] = [[False, random.randint(0, 1)], [False, random.randint(0, 1)], [False, random.randint(0, 1)], \
#     #   [False, random.randint(0, 1)], [False, random.randint(0, 1)], \
#     #   [False, random.randint(0, 1)], [False, random.randint(0, 1)]]
#     # board[1] =
#     # board[2] =
#     # board[3] =
#     # board[4] =
#     # board[5] =
#     # board[6] =
#
#
#     game_board = [board[0], board[1], board[2], board[3], board[4], board[5], board[6]]
#
#     return game_board

def create_game_board(height, width, mines=None):
    # below is a docstring
    """
    Create a gameboard of a specified size, with a specified number of mines
    :param height: number of rows -- 1 indexed
    :param width: number of columns -- 1 indexed
    :param mines: Optional number of mines to lay on the board. Default is 10%
    """

    # how many tiles the board needs
    num_tiles = height * width
    if not mines:
        mines = num_tiles / 10
    else:
        assert mines < num_tiles

    # each tile list has the meaning: [Visible (bool), Mine (bool), Adjacent Mines (int)]
    # THERE IS A CRAZY BUG HERE! when multiplying lists, python doesn't create a copy, but instead passes by referece
    # this means if you change any of these lists, it affects the rest.
    # tiles = ([[False, True, 0]] * mines) + ([[False, False, 0]] * (num_tiles - mines))
    # Instead use this... these should not be references to the same list but instead independant lists.
    tiles = [[False, True, 0] for _ in range(mines)] + [[False, False, 0] for _ in range(num_tiles - mines)]

    # now randomize the list's order, so we can just use pop() to take from the list. Right now, the list is all mines
    # first, then all non mines, which would be a bit too easy
    random.shuffle(tiles)
    # this is an inplace function, meaning that it changes the value of the thing it's passed

    # initialize the board as an empty list
    game_board = list()

    for i in range(height):
        # pop() removes the end of the list and returns the value it removed to you
        # for _ in range(N) is the idiom for when you want to iterate N times but don't care about the iterators value
        # here, _ means "I don't give a shit what the value is"
        game_board.append([tiles.pop() for _ in range(width)])

    # the one problem left is how to calculate the number of neighbors that a given tile has, that are mines
    # this problem is left to the reader, but I'll give you some hints: see get neighbors below

    return game_board


def get_neighbors(game_board, row_idx, col_idx):
    """
    for a given game board and tile location, get the neighbors without going out of bounds of the board
    :param game_board: the game board
    :param row_idx: row index number of the tile in question
    :param col_idx: column index number of the tile in question
    :returns list of lists [(row_idx, col_idx), tile value] for the neighbors
    """

    # bounds for where neighbors could be (min_row_num, max_row_num). You need to protect against this edge case:
    # [1,2,3,4][-1:1] --> []
    # the index method [list of things][start:finish:step] works here, but if fails when you start with a negative
    # and finish with a positive when you don't have a step that's negative.
    # the same issue doesn't exist for the finish > length case
    height = len(game_board) - 1
    width = len(game_board[0]) - 1
    row_min = row_idx - 1 if row_idx > 0 else 0
    row_max = row_idx + 1 if row_idx < height else height
    col_min = col_idx - 1 if col_idx > 0 else 0
    col_max = col_idx + 1 if col_idx < width else width

    neighbors = list()
    #now make the coordinates and get the values
    for row_num in range(row_min, row_max + 1):
        for col_num in range(col_min, col_max + 1):
            if row_num == row_idx and col_num == col_idx:
                #we don't want the central tile
                pass
            neighbors.append([(row_num, col_num), game_board[row_num][col_num]])

    return neighbors


# Nothing fundamentally wrong with this approach, it is just simpler to use a generator with a render_tile function
# # Handle hiding and revealing spaces
# def interpret_row(row):
#     for i in row:
#         if not i[0]:
#             print"[O]",
#         else:
#             if i[-1] == 0:
#                 print"[ ]",
#             else:
#                 print"[X]",

def render_tile(tile):
    """
    For a given tile, render it's character
    :param tile:
    :returns str value of tile
    """

    # each tile list has the meaning: [Visible (bool), Mine (bool), Adjacent Mines (int)]
    # visible, mine, adjacent_mines = tile

    if tile[0]:
        if tile[1]:
            return "X"
        elif tile[2]:
            return str(tile[2])
        else:
            return " "
    else:
        return "O"


# Handle player input
def click_space(game_board):

    # What happens if I enter a negative number here?
    mine_x = input("Enter Row:")

    while mine_x > len(game_board) - 1:
        mine_x = input("Too Large, Try Again")

    mine_y = input("Enter Column")

    while mine_y > len(game_board[mine_x]) - 1:
        mine_y = input("Too Large, Try Again")

    print game_board[mine_x][mine_y]
    game_board[mine_x][mine_y][0] = True
    if game_board[mine_x][mine_y][1]:
        # hit a mine!
        game_on = False
    else:
        game_on = True

    return game_board, game_on


# # Game over
# def game_over(game_board):
#     for i in game_board:
#         for j in i:
#             if j[-1] == 1:
#                 # Not sure what you are doing here
#                 j[0] = True
#
#     print "Game Over"
#     draw_grid(game_board)
#     game_on = False


def generate_board():
    rows = input("Enter number of rows:")
    cols = input("Enter number of columns:")
    mines = input("Enter number of mines:")

    try:
        assert isinstance(mines, int), "Mines must be an integer!"
        assert mines > 1, "Mines must be positive!"
        assert isinstance(rows, int), "Rows must be an integer!"
        assert rows > 1, "Rows must be positive!"
        assert isinstance(cols, int), "Columns must be an integer!"
        assert cols > 1, "Columns must be positive!"
    except AssertionError as e:
        print e.message
        game_on = False
        game_board = None
        return game_on, game_board

    game_on = True
    game_board = create_game_board(rows, cols, mines=mines)
    return game_on, game_board

# Output test
#   draw_grid(random_mines(game_board))


if __name__ == "__main__":
    # it is really important that you do this if name == main thing. It's a distinguishing feature of those who script
    # vs those who code. You are the latter. If you don't know what this idiom does, google it.

    while True:

        # Game test
        print "".join(["-"]*11)
        print "Minesweeper"

        game_on, game_board = generate_board()
        # nothing technically wrong here, just made a lot of changes
        # draw_grid(random_mines(game_board))
        if game_on:
            render_board(game_board)

        while game_on:
            game_board, game_on = click_space(game_board)
            render_board(game_board)

            if not game_on:
                print "Sorry, you lose!"
