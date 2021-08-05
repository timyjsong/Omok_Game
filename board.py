import tkinter as tk
from square import Square

class Board(tk.Canvas):

    def __init__(self, master, board_size):
        self.master = master
        self.board_size = board_size
        super().__init__(master, width=board_size, height=board_size)
        self.bind("<Button-1>", self.left_click)
        self.pack()
        self.squares = self.init_squares()
        self.draw_squares()

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




