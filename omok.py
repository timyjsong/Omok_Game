import tkinter as tk
from board import Board

"""
requirements:

win condition: 5 in a row, horizonal, vertical, diagonal
turn counter
checking if game won: after every turn
board size: 19 x 19
3 classes: 1 for drawing, 1 for points (coords), 1 for pieces
"""


def main():
    root = tk.Tk()
    root.geometry("900x900")
    board = Board(root, 840) # 14 x 60 = 840
    root.mainloop()


if __name__ == "__main__":
    main()



