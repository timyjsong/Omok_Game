""" Module for Board class"""
# pylint: disable=too-many-ancestors

import tkinter as tk
from square import Square
from piece import Piece


class Board(tk.Canvas):
    """ Class for Board"""

    total_squares = 14

    def __init__(self, master, window_size, logger):
        self.master = master
        self.window_size = window_size
        self.logger = logger.get_logger("board")

        self.board_size = (window_size * 14) / 15
        super().__init__(master, width=window_size, height=window_size)
        self.bind("<Button-1>", self.left_click)
        self.turn = 0
        self.pieces = []
        self.squares = self.init_squares()
        self.draw_border()
        self.draw_squares()

    @property
    def square_len(self):
        """ returns the length of one square"""

        return self.board_size / self.total_squares

    def draw_border(self):
        """ given a canvas, draws a border around the playable squares"""

        coords = (0, 0, self.window_size, self.window_size)
        self.create_rectangle(*coords, fill="#8C5024")

    def init_squares(self):
        """ returns a list of squares in which the board will be made out"""

        squares = []
        for row in range(14):
            for col in range(14):
                square = Square(self, row, col)
                squares.append(square)

        return squares

    def left_click(self, event):
        """ following certain playable rules, draws pieces onto the board upon left click"""

        color = "black" if not self.turn % 2 else "white"
        print(f"turn: {color}")

        square = self.find_square(event.x, event.y)
        try:
            corner = square.find_corner(event.x, event.y)
        except Exception as error:
            self.logger.exception(error)
            raise error

        piece = Piece(self, *corner, color)
        try:
            self.piece_exist(piece.corner)
        except Exception as error:
            self.logger.exception(error)
            raise error

        piece.draw()
        self.pieces.append(piece)
        self.turn += 1

    def draw_squares(self):
        """ fills in an empty board/canvas with playable squares"""

        for square in self.squares:
            square.draw()

    def find_square(self, c_x, c_y):
        """ given x and y coordinate, finds which square the left_click is in"""

        for square in self.squares:
            if square.in_square(c_x, c_y):
                return square

        raise Exception("Square not found")

    def piece_exist(self, corner):
        """ checker to see if piece already exists on a specific board location"""

        for piece in self.pieces:
            if piece.corner == corner:
                raise Exception("Piece already exists there")
