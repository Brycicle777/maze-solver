from cell import Cell
import time


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = [[None for j in range(
            0, self.num_rows)] for i in range(0, self.num_cols)]
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                new_cell = Cell(self._x1 + i * self.cell_size_x,
                                self._x1 + i * self.cell_size_x + self.cell_size_x,
                                self._y1 + j * self.cell_size_y,
                                self._y1 + j * self.cell_size_y + self.cell_size_y,
                                self._win)
                self._cells[i][j] = new_cell
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
