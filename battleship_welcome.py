"""
welcome screen for battleship opens battleship file
file:battleship_welcomeeasy.py
by:olivia brazak
"""

import battleship


def welcome():
    print("XXXXX   XXXX  XXXXXX XXXXXX XX     XXXXX   XXXXX XX  XX XX XXXXX")
    print("XX  XX XX  XX   XX     XX   XX     XX     XX     XX  XX XX XX  XX")
    print("XXXXX  XXXXXX   XX     XX   XX     XXXX    XXXX  XXXXXX XX XXXXX")
    print("XX  XX XX  XX   XX     XX   XX     XX         XX XX  XX XX XX")
    print("XXXXX  XX  XX   XX     XX   XXXXX  XXXXX  XXXXX  XX  XX XX XX\n")
    print("    .  o ..                  ")
    print("    o . o o.o                ")
    print("          ...oo              ")
    print("            __[]__           ")
    print("         __|_o_o_o\__        ")
    print("         \\o  o o   o/       ")
    print("          \\. ..  . /        ")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")


def start():
    input("Press ENTER to start the game")


def main():
    welcome()
    start()
    board = battleship.create_board()
    board2 = battleship.create_board()
    ai = battleship.setup(board, board2)
    battleship.turns(board, board2, ai)

main()