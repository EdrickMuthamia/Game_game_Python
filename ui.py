from game_logic import GoBoard
from models import save_game

def print_board(board):
    # Print column numbers
    print("  " + " ".join(str(i) for i in range(board.size)))
     # Print each row with row number
    for row in range(board.size):
        symbols = []
        for cell in board.board[row]:
            if cell == 0:
                symbols.append(".")
            elif cell == 1:
                symbols.append("B")
            else:
                symbols.append("W")
        print(f"{row} " + " ".join(symbols))