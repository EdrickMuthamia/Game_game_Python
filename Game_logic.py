class GoBoard:
    def __init__(self):
        self.size = 9  # 9x9 board
        self.board = []  # Create empty board
        row = 0
        while row < 9:
            new_row = []
            col = 0
            while col < 9:
                new_row.append(0)  # 0=empty, 1=black, 2=white
                col = col + 1
            self.board.append(new_row)
            row = row + 1
        self.current_player = 1  # 1=black, 2=white
        self.passes = 0  # Count passes
        self.captured_black = 0  # Black stones captured by white
        self.captured_white = 0  # White stones captured by black
        print("New 9x9 Go board created.")
    def place_stone(self, x, y):
        # Check if the move is outside the board
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            print("This spot is not on the board.")
            return False

        # Check if the spot is already taken
        if self.board[x][y] != 0:
            print("This spot already has a stone.")
            return False

        # Put the stone of the current player on the board
        self.board[x][y] = self.current_player

        # Look at the 4 sides (up, down, left, right)
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        # Keep track of captured stones
        captured = 0

        # Check each neighbor
        for nx, ny in neighbors:
            # Make sure neighbor is inside the board
            if 0 <= nx < self.size and 0 <= ny < self.size:
                # If neighbor is the other player
                if self.board[nx][ny] != 0 and self.board[nx][ny] != self.current_player:
                    # If that stone has no empty space around it, capture it
                    if not self.has_liberty(nx, ny, self.board[nx][ny]):
                        self.remove_group(nx, ny, self.board[nx][ny])
                        captured += 1

        # Switch turns
        if self.current_player == 1:
            color = "Black"
            self.current_player = 2
        else:
            color = "White"
            self.current_player = 1

        print(color, "stone placed at (", x, ",", y, "). Captured", captured, "stones.")
        return True
   