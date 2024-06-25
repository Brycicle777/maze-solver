from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
#    line_one = Line(Point(200, 50), Point(600, 50))
    #win.draw_line(line_one, "red")
    #line_two = Line(Point(400, 50), Point(400, 500))
    #win.draw_line(line_two, "red")
    test_cell = Cell(50, 750, 50, 400, win)
    test_cell.draw()
    win.wait_for_close()

main()
