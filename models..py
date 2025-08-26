from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
import json


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
    winner_id = Column(Integer, ForeignKey('users.id'))
    captures = Column(String)

    # Save captures in text form
    def save_captures(self, captured):
        if captured:
            self.captures = json.dumps(captured)
        else:
            self.captures = "{}"

    # Load captures back into dictionary form
    def load_captures(self):
        if self.captures:
            return json.loads(self.captures)
        else:
            return {"black_captures": 0, "white_captures": 0}
