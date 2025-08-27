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
        
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            print("This spot is not on the board.")
            return False
        if self.board[x][y] != 0:
            print("This spot already has a stone.")
            return False

        self.board[x][y] = self.current_player

        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        captured = 0

        for nx, ny in neighbors:
            
            if 0 <= nx < self.size and 0 <= ny < self.size:
                
                if self.board[nx][ny] != 0 and self.board[nx][ny] != self.current_player:
                   
                    if not self.has_liberty(nx, ny, self.board[nx][ny]):
                        self.remove_group(nx, ny, self.board[nx][ny])
                        captured += 1

        
        if self.current_player == 1:
            color = "Black"
            self.current_player = 2
        else:
            color = "White"
            self.current_player = 1

        print(color, "stone placed at (", x, ",", y, "). Captured", captured, "stones.")
        return True
    def has_liberty(self, x, y, color):
       
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for nx, ny in neighbors:
            if 0 <= nx < self.size and 0 <= ny < self.size:
                if self.board[nx][ny] == 0: 
                    return True
        return False
    
    def remove_group(self, x, y, color):
        
        if self.board[x][y] != color:
            return
        self.board[x][y] = 0  # remove stone
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for nx, ny in neighbors:
            if 0 <= nx < self.size and 0 <= ny < self.size:
                self.remove_group(nx, ny, color)
    
    def pass_turn(self):
        self.passes = self.passes + 1
        if self.current_player == 1:
            color = "black"
            self.current_player = 2
        else:
            color = "white"
            self.current_player = 1
        print(f"Player {color} passed.")
    def is_game_over(self):
        if self.passes >= 2:
            print("Game over: two passes in a row.")
            return True
        else:
            return False
