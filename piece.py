""" Module for Piece class to keep track of coordinates """


class Piece:
    """ Class for Piece"""

    piece_size = 0.41

    def __init__(self, canvas, c_x, c_y, color):
        self.canvas = canvas
        self.color = color
        self.c_x, self.c_y = c_x, c_y

    def __str__(self):
        return f"{self.c_x}, {self.c_y}"

    @property
    def corner(self):
        """ returns the x, y coordinates of the piece"""

        return round(self.c_x, 4), round(self.c_y, 4)

    @property
    def spacing(self):
        """
        returns the spacing which will be used to create
        spacing between adjacent pieces
        """

        return self.canvas.square_len * self.piece_size

    # @property
    # def offset(self):
    #     """ returns the offset of the border"""
    #
    #     return self.canvas.square_len / 2

    @property
    def center(self):
        """ returns the coordinates of the piece in row/col format"""

        row_coord = self.c_x - (self.canvas.square_len / 2)
        row = round(row_coord / self.canvas.square_len)
        col_coord = self.c_y - (self.canvas.square_len / 2)
        col = round(col_coord / self.canvas.square_len)

        return row, col

    @property
    def x_1(self):
        """ top left x coordinate of the piece"""

        return self.c_x - self.spacing

    @property
    def y_1(self):
        """ top left y coordinate of the piece"""

        return self.c_y - self.spacing

    @property
    def x_2(self):
        """ bottom right x coordinate of the piece"""

        return self.c_x + self.spacing

    @property
    def y_2(self):
        """ bottom right y coordinate of the piece"""

        return self.c_y + self.spacing

    @property
    def coords(self):
        """ returns the top left and bottom right (x,y) coordinates"""

        return self.x_1, self.y_1, self.x_2, self.y_2

    def draw(self):
        """ draws a piece onto the board"""

        self.canvas.create_oval(*self.coords, fill=self.color)
