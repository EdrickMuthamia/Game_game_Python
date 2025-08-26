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
