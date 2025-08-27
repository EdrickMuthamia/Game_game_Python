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

def handle_play_game(session):
    # Handle the play game option.
    p1, p2 = get_player_names()
    if p1 and p2:
        player1 = add_user(session, p1)
        player2 = add_user(session, p2)
        if player1 and player2:
            play_game(player1, player2, session)

def handle_view_stats(session):
    #Handle the view stats option.
    name = input("Enter name: ").strip()
    if name:
        wins, losses = get_user_stats(session, name)
        print(f"{name}: Wins {wins}, Losses {losses}")
    else:
        print("Name cannot be empty.")

def main():
    # Initialize database
    Session = init_db()
    if not Session:
        print("Database initialization failed.")
        return

    session = Session()

    menu_options = {
        '1': handle_play_game,
        '2': handle_view_stats
    }
    while True:
        print("\nGo Game Menu:")
        print("1. Play Game")
        print("2. View User Stats")
        print("3. Exit")

        choice = input("Choose: ").strip()

        if choice == '3':
            print("Thank You For Playing Go Game")
            session.close()
            break
        elif choice in menu_options:
            menu_options[choice](session)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
