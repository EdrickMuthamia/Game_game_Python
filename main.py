from database import init_db
from models import add_user, get_user_stats
from ui import play_game

def get_player_names():
    #Get and validate player names.
    p1 = input("Player 1 (Black) name: ").strip()
    p2 = input("Player 2 (White) name: ").strip()

    if not p1 or not p2:
        print("Both player names are required.")
        return None, None

    if p1 == p2:
        print("Player names must be different.")
        return None, None

    return p1, p2