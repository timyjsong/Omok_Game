""" Module for Board class"""
# pylint: disable=too-many-ancestors

import tkinter as tk
from square import Square
from piece import Piece


class Board(tk.Canvas):
    """ Class for Board"""

    total_squares = 14
    gameover = False

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

        if self.gameover:
            return

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

        self.logger.info(f"{piece.center}")

        piece.draw()
        self.pieces.append(piece)
        self.gameover = self.check_win()

        self.turn += 1

    def draw_squares(self):
        """ fills in an empty board/canvas with playable squares"""

        for square in self.squares:
            square.draw()

    def find_square(self, c_x, c_y):
        """ given x and y coordinate, finds which square the left_click is in"""

        ret = None
        self.logger.debug(f"find square, X: {c_x}, Y: {c_y}")
        for square in self.squares:
            if square.in_square(c_x, c_y):
                return square

        t_x, t_y = self.find_border(c_x, c_y)
        for square in self.squares:
            if square.in_square(t_x, t_y):
                return square

        raise Exception("Square not found")

    def find_border(self, c_x, c_y):
        """ given that left_click has occurred on the border, finds the closest corner"""

        sq_len = self.square_len
        window_size = self.window_size
        board_size = self.board_size
        t_x = c_x
        t_y = c_y

        # finding which side of the border left_click occurred
        if c_x < (sq_len / 2):
            # x is on left border
            if c_y < (sq_len / 2):
                # y is on top border
                t_x = sq_len - c_x
                t_y = sq_len - c_y
            elif c_y > (window_size - (sq_len / 2)):
                # y is on bottom border
                t_x = sq_len - c_x
                t_y = (2 * board_size) + sq_len - c_y
            else:
                # y is on the board
                t_x = sq_len - c_x
        elif c_x > (window_size - (sq_len / 2)):
            # x is on right border
            if c_y > (window_size - (sq_len / 2)):
                # y is on bottom border
                t_x = (2 * board_size) + sq_len - c_x
                t_y = (2 * board_size) + sq_len - c_y
            elif c_y < (sq_len / 2):
                # y is on top
                t_x = (2 * board_size) + sq_len - c_x
                t_y = sq_len - c_y
            else:
                # y is on the board
                t_x = (2 * board_size) + sq_len - c_x
        else:
            # x is on board
            if c_y < (sq_len / 2):
                # y is on top border
                t_y = sq_len - c_y
            else:
                # y is on bottom border
                t_y = (2 * board_size) + sq_len - c_y

        return t_x, t_y

    def piece_exist(self, corner):
        """ checker to see if piece already exists on a specific board location"""

        for piece in self.pieces:
            if piece.corner == corner:
                raise Exception("Piece already exists there")

    def check_win(self):
        return False
