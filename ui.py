from game_logic import GoBoard
from models import save_game

def print_board(board):
    
 print("  " + " ".join(str(i) for i in range(board.size)))

     
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

        def get_move(current_player):player_name = "Black" if current_player == 1 else "White"

    for attempt in range(3):
        move = input(f"Player {player_name}, enter move (x y) or 'pass': ").strip()

        if move.lower() == "pass":
            return None

        parts = move.split()
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            x, y = int(parts[0]), int(parts[1])
            if x >= 0 and y >= 0:
                return x, y
            print("Invalid input. Use format '3 4' or 'pass'.")

    return None

def play_game(player1, player2, session):
    if not player1 or not player2:
        print("Error: Both players are required.")
        return

    board = GoBoard()
    print_board(board)

    
    while not board.is_game_over():
        move = "get_move"(board.current_player)
        player_name = "Black" if board.current_player == 1 else "White"

        if move is None:
            print(f"Player {player_name} passes.")
            board.pass_turn()
        else:
            x, y = move
            if board.place_stone(x, y):
                color = "black" if board.current_player == 1 else "white"
                print(f"Placed {color} stone at ({x}, {y}).")
            else:
                print("Invalid move. Try again.")
                continue

        print_board(board)

    
    black_score, white_score = board.calculate_score()
    print(f"Scores: Black {black_score}, White {white_score}")

    if black_score > white_score:
        winner, winner_name = player1, player1.name
    elif white_score > black_score:
        winner, winner_name = player2, player2.name
    else:
        winner, winner_name = None, "Tie game"

    print(f"Winner: {winner_name}")

    captures = {
        "black_captures": board.captured_black,
        "white_captures": board.captured_white
    }
    save_game(session, player1, player2, winner, captures)

    print(f"Captures: Black {board.captured_black}, White {board.captured_white}")
    print(f"{player1.name} stats: Wins {player1.wins}, Losses {player1.losses}")
    print(f"{player2.name} stats: Wins {player2.wins}, Losses {player2.losses}")


