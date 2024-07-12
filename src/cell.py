from tkinter import Tk, BOTH, Canvas
from point import Point
from line import Line


class Cell:
    def __init__(self, x1, x2, y1, y2, win=None, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.visited = False

    def draw(self):
        if self._win:
            if self.has_left_wall:
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)).draw(
                    self._win.canvas, "black")
            else:
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)).draw(
                    self._win.canvas, "#D9D9D9")
            if self.has_right_wall:
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)).draw(
                    self._win.canvas, "black")
            else:
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)).draw(
                    self._win.canvas, "#D9D9D9")
            if self.has_top_wall:
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)).draw(
                    self._win.canvas, "black")
            else:
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)).draw(
                    self._win.canvas, "#D9D9D9")
            if self.has_bottom_wall:
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)).draw(
                    self._win.canvas, "black")
            else:
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)).draw(
                    self._win.canvas, "#D9D9D9")


    def draw_move(self, to_cell, undo=False):
        if self._win:
            from_cell_center_point = Point(
                (self._x2 - self._x1) / 2 + self._x1, (self._y2 - self._y1) / 2 + self._y1)
            to_cell_center_point = Point(
                (to_cell._x2 - to_cell._x1) / 2 + to_cell._x1, (to_cell._y2 - to_cell._y1) / 2 + to_cell._y1)
            fill_color = "red" if undo is False else "gray"
            Line(from_cell_center_point, to_cell_center_point).draw(
                self._win.canvas, fill_color)
