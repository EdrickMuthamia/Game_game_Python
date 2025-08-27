from game_logic import GoBoard
from models import save_game

def print_board(board):
    # Print column numbers
    print("  " + " ".join(str(i) for i in range(board.size)))