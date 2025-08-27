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
        