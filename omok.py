""" Module for Omok class which includes main"""

import tkinter as tk
from board import Board


class Window(tk.Tk):
    """ Class for tkinter window"""

    def __init__(self, window_size):
        super().__init__()
        self.geometry(f"{window_size}x{window_size}")
        board = Board(self, window_size)
        board.pack()


def main():
    """ Main"""

    window = Window(900)
    window.mainloop()


if __name__ == "__main__":
    main()
