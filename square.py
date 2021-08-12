""" Module for Square class"""


class Square:
    """ Class for Square"""

    color = "#A9602B"

    def __init__(self, canvas, row, col):
        self.canvas = canvas
        self.row, self.col = row, col
        self.side_len = canvas.square_len

    def __str__(self):
        return f"row: {self.row}, col: {self.col}"

    @property
    def x_1(self):
        """ returns the top left x coordinate of the square"""

        return self.side_len * self.col + (self.side_len / 2)

    @property
    def y_1(self):
        """ returns the top left y coordinate of the square"""

        return self.side_len * self.row + (self.side_len / 2)

    @property
    def x_2(self):
        """ returns the bottom right x coordinate of the square"""

        return self.x_1 + self.side_len

    @property
    def y_2(self):
        """ returns the bottom right y coordinate of the square"""

        return self.y_1 + self.side_len

    @property
    def coords(self):
        """ returns the top left (x_1,y_1) & the bottom right (x_2,y_2) coordinates"""

        return self.x_1, self.y_1, self.x_2, self.y_2

    @property
    def corners(self):
        """ returns a set of 4 coordinates each depicting the 4 corners of the square"""

        return [(self.x_1, self.y_1), (self.x_1, self.y_2),
                (self.x_2, self.y_1), (self.x_2, self.y_2)]

    def draw(self):
        """ draws the square with its known coordinates"""

        self.canvas.create_rectangle(*self.coords, fill=self.color)

    def in_square(self, c_x, c_y):
        """ returns whether given coordinates are within the square"""

        is_in_x = self.x_1 <= c_x <= self.x_2
        is_in_y = self.y_1 <= c_y <= self.y_2
        return is_in_x and is_in_y

    def find_corner(self, c_x, c_y):
        """ given coordinates, finds and returns the closest corner of the square"""

        x1_dist = c_x - self.x_1
        x2_dist = self.x_2 - c_x
        y1_dist = c_y - self.y_1
        y2_dist = self.y_2 - c_y

        if (x1_dist == x2_dist) or (y1_dist == y2_dist):
            raise Exception("Clicked in the middle")

        x_coord = self.x_1 if x1_dist < x2_dist else self.x_2
        y_coord = self.y_1 if y1_dist < y2_dist else self.y_2

        return x_coord, y_coord
