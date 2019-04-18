"""
battleship game
file: battleship.py
by: olivia brazak
"""
import random as rand


def create_board():
    board = []
    for i in range(0,8):
        board.append([0]*8)

    return board


def print_board(board):
    for i in board:
        print(i)


def p1smallship_placement(board):
    print("Please pick coordinates for three small ships by using two numbers in the format: x,y,x,y:\n")
    x1, y1, x2, y2 = [int(x) for x in input("Where on the board would you like to place the first small ship?").split(',')]

    board[y1][x1] = 1
    board[y2][x2] = 1

    x3, y3, x4, y4 = [int(x) for x in input("Where on the board would you like to place the second small ship?").split(',')]

    board[y3][x3] = 1
    board[y4][x4] = 1

    x5, y5, x6, y6 = [int(x) for x in input("Where on the board would you like to place the third small ship?").split(',')]

    board[y5][x5] = 1
    board[y6][x6] = 1

    print("Your game board now looks like this: \n")
    print_board(board)

    x = input("Is the correct(Y/N)? ")
    if x == "N":
        p1smallship_placement(board)


def p1mediumship_placement(board):
    print("Please pick coordinates for two medium ships by using three numbers in the format x,y,x,y,x,y :\n")
    x7, y7, x8, y8, x9, y9 = [int(x) for x in input("Where would you like to place the first medium ship?").split(',')]

    board[y7][x7] = 1
    board[y8][x8] = 1
    board[y9][x9] = 1

    x10, y10, x11, y11, x12, y12 = [int(x) for x in input("Where would you like to place the second medium ship?").split(',')]

    board[y10][x10] = 1
    board[y11][x11] = 1
    board[y12][x12] = 1

    print("Your game board now looks like this: \n")
    print_board(board)

    x = input(print("Is the correct(Y/N)? "))
    if x == "N":
        p1mediumship_placement(board)


def p1largeship_placement(board):
    print("Please pick coordinates for one large ship by using four numbers in the format x,y,x,y,x,y,x,y:\n")
    x13, y13, x14, y14, x15, y15, x16, y16 = [int(x) for x in input("Where would you like to place the large ship?").split(',')]

    board[y13][x13] = 1
    board[y14][x14] = 1
    board[y15][x15] = 1
    board[y16][x16] = 1

    print("Your game board now looks like this: \n")
    print_board(board)

    x = input(print("Is the correct(Y/N)? "))
    if x == "N":
        p1largeship_placement(board)


def p2smallship_placement(board):
    print("Please pick coordinates for three small ships by using two numbers in the format: x,y,x,y:\n")
    x1, y1, x2, y2 = [int(x) for x in input("Where on the board would you like to place the first small ship?").split(',')]

    board[y1][x1] = 1
    board[y2][x2] = 1

    x3, y3, x4, y4 = [int(x) for x in input("Where on the board would you like to place the second small ship?").split(',')]

    board[y3][x3] = 1
    board[y4][x4] = 1

    x5, y5, x6, y6 = [int(x) for x in input("Where on the board would you like to place the third small ship?").split(',')]

    board[y5][x5] = 1
    board[y6][x6] = 1

    print("Your game board now looks like this: \n")
    print_board(board)

    x = input("Is the correct(Y/N)? ")
    if x == "N":
        p1smallship_placement(board)


def p2mediumship_placement(board):
    print("Please pick coordinates for two medium ships by using three numbers in the format x,y,x,y,x,y :\n")
    x7, y7, x8, y8, x9, y9 = [int(x) for x in input("Where would you like to place the first medium ship?").split(',')]

    board[y7][x7] = 1
    board[y8][x8] = 1
    board[y9][x9] = 1

    x10, y10, x11, y11, x12, y12 = [int(x) for x in input("Where would you like to place the second medium ship?").split(',')]

    board[y10][x10] = 1
    board[y11][x11] = 1
    board[y12][x12] = 1

    print("Your game board now looks like this: \n")
    print_board(board)

    x = input("Is the correct(Y/N)? ")
    if x == "N":
        p2mediumship_placement(board)


def p2largeship_placement(board):
    print("Please pick coordinates for one large ship by using four numbers in the format x,y,x,y,x,y,x,y:\n")
    x13, y13, x14, y14, x15, y15, x16, y16 = [int(x) for x in input("Where would you like to place the large ship?").split(',')]

    board[y13][x13] = 1
    board[y14][x14] = 1
    board[y15][x15] = 1
    board[y16][x16] = 1

    print("Your game board now looks like this: \n")
    print_board(board)

    x = input("Is the correct(Y/N)? ")
    if x == "N":
        p2largeship_placement(board)


def setup(board, board2):
    username = input("Please enter player 1s username: ")
    print("Hello", username, "let's get started\n")

    print("You have six ships to place on this board going horizontally or vertically: \n")
    print_board(board)
    print("")

    print("For now we will assign every 'X' to a number. \n")
    print("")

    p1smallship_placement(board)

    p1mediumship_placement(board)

    p1largeship_placement(board)

    x = input("Are there two players(Y/N)? ")
    if x == "Y":
        username2 = input("Please enter player2s username: ")
        print("Hello", username2, "let's get started\n")

        print("You have six ships to place on this board going horizontally or vertically: \n")
        print_board(board2)
        print("")

        print("For now we will assign every 'X' to a number. \n")
        print("")

        p2smallship_placement(board2)

        p2mediumship_placement(board2)

        p2largeship_placement(board2)
        return False

    else:
        ai_shipplacement(board2)
        return True


"""
def ai_shipplacement(board):
    x = rand.randint(0,8)
    y = rand.randint(0,8)
    dir = rand.randint(0,4)
    
    x1 =
    y1 =
    x2 =
    y2 =
    board[y1][x1] = 1
    board[y2][x2] = 1

    x3 =
    y3 =
    x4 =
    y4 =
    board[y3][x3] = 1
    board[y4][x4] = 1

    x5 =
    y5 =
    x6 =
    y6 =
    board[y5][x5] = 1
    board[y6][x6] = 1
    
    
    x7 = 
    y7 =
    x8 =
    y8 =
    x9 =
    y9 =
    board[y7][x7] = 1
    board[y8][x8] = 1
    board[y9][x9] = 1
    
    x10 =
    y10 =
    x11 =
    y11 =
    x12 = 
    y12 =
    board[y10][x10] = 1
    board[y11][x11] = 1
    board[y12][x12] = 1

    x13 =
    y13 =
    x14 =
    y14 =
    x15 =
    y15 =
    x16 = 
    y16 =
    board[y13][x13] = 1
    board[y14][x14] = 1
    board[y15][x15] = 1
    board[y16][x16] = 1
"""


def ai_shipplacement(board):
    for length, quantity in [(2, 3), (3, 2), (4, 1)]:
        for _ in range(0, quantity):
            x = rand.randint(length, 8 - length)
            y = rand.randint(length, 8 - length)
            dir = rand.randint(0, 3)

            for _ in range(0, length):
                board[y][x] = 1

                # up
                if dir == 0:
                    y = y-1

                # right
                elif dir == 1:
                    x = x + 1

                # down
                elif dir == 2:
                    y = y + 1

                # left
                else:
                    x = x - 1


def is_alive(board):
    for row in board:
        if 1 in row:
            return True
    return False


def blind(board):
    return [[0 if place == 1 else place for place in row] for row in board]


def turns(board, board2, ai):

    while is_alive(board) and is_alive(board2):
        print("Player 1 choose where to hit in x,y format: ")
        print_board(blind(board2))
        print("-------------------")
        print_board(board)
        print("")
        hit(board2)

        if not ai:
            print("Player 2 choose where to hit in x,y format: ")
            print_board(blind(board))
            print("-------------------")
            print_board(board2)
            print("")
            hit(board)
        else:
            ai_hit(board)

    else:
        if is_alive(board):
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")


def hit(board):
    x1, y1 = [int(x) for x in input("Where would you like to hit?").split(',')]
    if board[y1][x1] == 1:
        board[y1][x1] = 4
        print("Hit! Please go again")
        hit(board)
    else:
        board[y1][x1] = 3


def ai_hit(board):
    x = rand.randint(0, 7)
    y = rand.randint(0, 7)
    if board[y][x] == 1:
        board[y][x] = 4
        dir = rand.randint(0, 4)
        # up
        if dir == 0:
            y = y - 1

        # right
        elif dir == 1:
            x = x + 1

        # down
        elif dir == 2:
            y = y + 1

        # left
        else:
            x = x - 1

        while x in range(0, 8) and y in range(0, 8) and board[y][x] == 1:
            board[y][x] = 4
            # up
            if dir == 0:
                y = y - 1

            # right
            elif dir == 1:
                x = x + 1

            # down
            elif dir == 2:
                y = y + 1

            # left
            else:
                x = x - 1
        print("Hit! Please go again")
        ai_hit(board)
    else:
        board[y][x] = 3
