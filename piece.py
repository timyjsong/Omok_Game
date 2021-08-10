

class Piece(object):

    piece_size = 0.41

    def __init__(self, canvas, c_x, c_y, color):
        self.canvas = canvas
        self.color = color
        self.c_x, self.c_y = c_x, c_y

    def __str__(self):
        return f"row: {self.c_x}, col: {self.c_y}"

    @property
    def offset(self):
        return self.canvas.square_len * self.piece_size

    @property
    def x_1(self):
        return self.c_x - self.offset

    @property
    def y_1(self):
        return self.c_y - self.offset

    @property
    def x_2(self):
        return self.c_x + self.offset

    @property
    def y_2(self):
        return self.c_y + self.offset

    @property
    def coords(self):
        return self.x_1, self.y_1, self.x_2, self.y_2

    def draw(self):
        print(f"circle: {self.coords}")
        self.canvas.create_oval(*self.coords, fill=self.color)

