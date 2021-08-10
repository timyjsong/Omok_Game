import tkinter as tk
from square import Square
from piece import Piece

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

    @property
    def square_len(self):
        return self.board_size // self.total_squares

    @property
    def total_board_size(self):
        return self.board_size + self.square_len

    def draw_border(self):
        coords = (0, 0, self.total_board_size, self.total_board_size)
        self.create_rectangle(*coords, fill="#8C5024")

    def init_squares(self):
        squares = []
        for row in range(14):
            for col in range(14):
                square = Square(self, row, col)
                squares.append(square)

        return squares

    def left_click(self, event):
        square = self.find_square(event.x, event.y)
        corner = square.find_corner(event.x, event.y)
        # color = "black" if not self.turn % 2 else "white"
        piece = Piece(self, *corner, "black")
        piece.draw()
        print(f"corner: {corner}")

    def draw_squares(self):
        for square in self.squares:
            square.draw()

    def find_square(self, c_x, c_y):
        for square in self.squares:
            if square.in_square(c_x, c_y):
                break
        else:
            raise Exception("Square not found")

        return square

