from chess_skeletons import *


chessboard0 = ChessBoard()
print(chessboard0._pieces)

# game_board = {}
#
# files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#
# for letter in files:
#     for num in range(1, 9):
#         game_board[(letter, num)] = '+'
#
# def board_printout(gameboard):
#     board = []
#     for num in range(1, 9):
#         rank = ""
#         for letter in files:
#             rank += gameboard[(letter, num)]
#         board.append(rank)
#         print(rank)
#     return board
#
# def init_board(gameboard):
#     pass
#
# board = board_printout(game_board)
