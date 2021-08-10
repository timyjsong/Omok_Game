

class Square(object):

    color = "#A9602B"

    def __init__(self, canvas, row, col):
        self.canvas = canvas
        self.row, self.col = row, col
        self.side_len = canvas.square_len

    def __str__(self):
        return f"row: {self.row}, col: {self.col}"

    @property
    def x_1(self):
        return self.side_len * self.col + (self.side_len / 2)

    @property
    def y_1(self):
        return self.side_len * self.row + (self.side_len / 2)

    @property
    def x_2(self):
        return self.x_1 + self.side_len

    @property
    def y_2(self):
        return self.y_1 + self.side_len

    @property
    def coords(self):
        return self.x_1, self.y_1, self.x_2, self.y_2

    @property
    def corners(self):
        return [(self.x_1, self.y_1), (self.x_1, self.y_2), (self.x_2, self.y_1), (self.x_2, self.y_2)]

    def draw(self):
        self.canvas.create_rectangle(*self.coords, fill=self.color)

    def in_square(self, c_x, c_y):
        is_in_x = (c_x >= self.x_1) and (c_x <= self.x_2)
        is_in_y = (c_y >= self.y_1) and (c_y <= self.y_2)
        return is_in_x and is_in_y

    def find_corner(self, c_x, c_y):
        x1_dist = c_x - self.x_1
        x2_dist = self.x_2 - c_x
        y1_dist = c_y - self.y_1
        y2_dist = self.y_2 - c_y

        if (x1_dist == x2_dist) or (y1_dist == y2_dist):
            raise Exception("Clicked in the middle")

        x_coord = self.x_1 if x1_dist < x2_dist else self.x_2
        y_coord = self.y_1 if y1_dist < y2_dist else self.y_2

        return x_coord, y_coord
