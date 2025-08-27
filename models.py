from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

# -----------------------------
# User table
# -----------------------------
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)

# -----------------------------
# Game table
# -----------------------------
class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer, ForeignKey('users.id'))
    player2_id = Column(Integer, ForeignKey('users.id'))
    winner_id = Column(Integer, ForeignKey('users.id'), nullable=True)  # Can be null for ties
    captures = Column(String)

    def save_captures(self, black, white):
        self.captures = f"{black},{white}"

    def load_captures(self):
        if not self.captures:
            return {"black_captures": 0, "white_captures": 0}
        black, white = self.captures.split(",")
        return {"black_captures": int(black), "white_captures": int(white)}

# -----------------------------
# Add or get existing user
# -----------------------------
def add_user(session, name):
    if not name:
        print("Error: Name cannot be empty.")
        return None
    # Check if user already exists
    existing_user = session.query(User).filter_by(name=name).first()
    if existing_user:
        return existing_user
    # Create new user
    user = User(name=name)
    session.add(user)
    session.commit()
    print(f"User {name} added successfully.")
    return user

# -----------------------------
# Save the game
# -----------------------------
def save_game(database, player1, player2, winner, captures):
    # Check if players exist
    if not player1 or not player2:
        print("Error: Both players are required!")
        return False
    # Create new game record
    game = Game()
    game.player1_id = player1.id
    game.player2_id = player2.id
    game.winner_id = winner.id if winner else None

    # Set captures
    black_captures = 0
    white_captures = 0
    if captures:
        if isinstance(captures, list) and len(captures) >= 2:
            black_captures = captures[0]
            white_captures = captures[1]
        elif isinstance(captures, dict):
            black_captures = captures.get("black_captures", 0)
            white_captures = captures.get("white_captures", 0)

    game.save_captures(black_captures, white_captures)
    database.add(game)

    # Update player records
    if winner == player1:
        player1.wins += 1
        player2.losses += 1
        print(f"{player1.name} wins!")
    elif winner == player2:
        player2.wins += 1
        player1.losses += 1
        print(f"{player2.name} wins!")
    else:
        print("It's a tie!")

    # Save to database
    database.commit()
    print("Game saved successfully!")
    return True

# -----------------------------
# Get a user's stats
# -----------------------------
def get_user_stats(session, name):
    if not name:
        print("Error: Name cannot be empty.")
        return 0, 0

    user = session.query(User).filter_by(name=name).first()

    if user:
        return user.wins, user.losses
    else:
        print(f"No user found with name {name}.")
        return 0, 0
# -----------------------------
# Get game history for a user
# -----------------------------
def get_user_games(session, name):
    if not name:
        return []

    user = session.query(User).filter_by(name=name).first()
    if not user:
        return []

    games = session.query(Game).filter(
        (Game.player1_id == user.id) | (Game.player2_id == user.id)
    ).all()

    if games:
        return games
    else:
        return []