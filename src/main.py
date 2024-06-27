from window import Window
from point import Point
from line import Line
from cell import Cell


def main():
    win = Window(800, 600)
    test_cell_one = Cell(50, 100, 50, 100, win, has_right_wall=False)
    test_cell_one.draw()
    test_cell_two = Cell(100, 150, 50, 100, win, has_left_wall=False)
    test_cell_two.draw()
    test_cell_one.draw_move(test_cell_two, undo=True)
    win.wait_for_close()


main()
