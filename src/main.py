from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze


def main():
    win = Window(600, 600)
    maze = Maze(50, 50, 10, 10, 50, 50, win)
    maze.solve()
    win.wait_for_close()
    


main()
