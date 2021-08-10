

class Square(object):

    side_len = 60
    color = "#A9602B"

    def __init__(self, canvas, row, col):
        self.canvas = canvas
        self.row, self.col = row, col

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

    def draw(self):
        self.canvas.create_rectangle(*self.coords, fill=self.color)





