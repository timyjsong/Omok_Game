""" Module for Board class"""
# pylint: disable=too-many-ancestors, too-many-instance-attributes

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

        self.logger.info(f"{piece.color} placed: {piece.center}")

        piece.draw()
        self.pieces.append(piece)
        self.gameover = self.check_win(piece)

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

    def check_win(self, piece):
        """ checks if recently placed piece satisfies the win condition"""

        vectors = [(-1, 0), (-1, 1), (0, 1), (1, 1)]

        pos_list = []

        for i in range(4):
            row, col = vectors[i]
            temp_list = self.get_possible_moves(piece, row, col)
            pos_list.append(temp_list[::-1])
            pos_list[i].append(piece.center)
            row, col = 0 - row, 0 - col
            temp_list = self.get_possible_moves(piece, row, col)
            pos_list[i] += temp_list

        for index in range(4):
            if self.is_five_in_row(pos_list[index]):
                self.logger.debug(f"{piece.color} HAS WON")
                return True

        return False

    @staticmethod
    def get_possible_moves(piece, row_delta, col_delta, total=5):
        """ given row and col delta, returns the possible moves"""

        row, col = piece.center
        ret_list = []
        for _ in range(total):
            row, col = row + row_delta, col + col_delta
            ret_list.append((row, col))

        return ret_list

    def is_five_in_row(self, pos_list):
        """ returns whether or not list of colors are 5 in a row"""

        color_list = []
        for pos in pos_list:
            color = self.find_piece(*pos)
            color_list.append(color)

        target_color = color_list[5]    # color of the last placed piece
        for index in range(7):
            if color_list[index] == target_color:
                counter = 1
                for index_2 in range(index + 1, 11):
                    if color_list[index_2] == target_color:
                        counter += 1
                    else:
                        break
                if counter == 5:
                    return True
        return False

    def find_piece(self, row, col):
        """ given row and col, returns the color of the piece, else returns None"""

        color = None
        for piece in self.pieces:
            if piece.center == (row, col):
                color = piece.color
                break

        return color
