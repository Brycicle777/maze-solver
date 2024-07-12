from cell import Cell
import time
import random


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._seed = random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

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
        if self._win:
            self._win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            cells_to_visit = []
            if i - 1 >= 0 and i - 1 < len(self._cells):
                if self._cells[i-1][j].visited == False:
                    cells_to_visit.append((i - 1, j)) 
            if j - 1 >= 0 and j - 1 < len(self._cells[i]):
                if self._cells[i][j-1].visited == False:
                    cells_to_visit.append((i, j - 1))
            if i + 1 >= 0 and i + 1 < len(self._cells):
                if self._cells[i+1][j].visited == False:
                    cells_to_visit.append((i + 1, j)) 
            if j + 1 >= 0 and j + 1 < len(self._cells[i]):
                if self._cells[i][j+1].visited == False:
                    cells_to_visit.append((i, j + 1))

            if cells_to_visit:
                dir = random.randrange(len(cells_to_visit))
                chosen_cell = cells_to_visit[dir]
                
                if chosen_cell[0] > i:
                    self._cells[i][j].has_right_wall = False
                    self._cells[chosen_cell[0]][chosen_cell[1]].has_left_wall = False
                elif chosen_cell[0] < i:
                    self._cells[i][j].has_left_wall = False
                    self._cells[chosen_cell[0]][chosen_cell[1]].has_right_wall = False
                else:
                    if chosen_cell[1] > j:
                        self._cells[i][j].has_bottom_wall = False
                        self._cells[chosen_cell[0]][chosen_cell[1]].has_top_wall = False
                    else:
                        self._cells[i][j].has_top_wall = False
                        self._cells[chosen_cell[0]][chosen_cell[1]].has_bottom_wall = False

                self._break_walls_r(chosen_cell[0], chosen_cell[1])
            else:
                self._draw_cell(i, j)
                break
