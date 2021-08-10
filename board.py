import tkinter as tk
from square import Square

class Board(tk.Canvas):

    total_squares = 14

    def __init__(self, master, board_size):
        self.master = master
        self.board_size = board_size
        super().__init__(master, width=self.total_board_size, height=self.total_board_size)
        self.bind("<Button-1>", self.left_click)
        self.pack()
        self.squares = self.init_squares()
        self.draw_border()
        self.draw_squares()
        # self.create_rectangle(0, 0, 1200, 1200, fill="green")

    @property
    def total_board_size(self):
        square_len = self.board_size // self.total_squares
        return self.board_size + square_len

    def draw_border(self):
        square_len = self.board_size // self.total_squares
        border_size = self.board_size + square_len
        coords = (0, 0, 1200, 1200)
        self.create_rectangle(*coords, fill="#8C5024")

    def init_squares(self):
        squares = []
        for row in range(14):
            for col in range(14):
                square = Square(self, row, col)
                squares.append(square)

        return squares

    def left_click(self, event):
        print(event.x, event.y)

    def draw_squares(self):
        for square in self.squares:
            square.draw()

