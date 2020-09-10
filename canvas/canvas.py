#!/usr/bin/env python3
import sys


class Canvas:

    def __init__(self):
        self.__columns = None
        self.__rows = None
        self.__matrix = None

    def init(self, width, height):
        self.__columns = width + 2
        self.__rows = height + 2
        self.__matrix = [[' ' for _ in range(self.__columns)] for _ in range(self.__rows)]
        for i in range(self.__rows):
            self.__matrix[i][0] = '|'
            self.__matrix[i][self.__columns - 1] = '|'
        for i in range(self.__columns):
            self.__matrix[0][i] = '-'
            self.__matrix[self.__rows - 1][i] = '-'

    def draw(self):
        result = ''
        for j in range(self.__rows):
            for i in range(self.__columns):
                result += self.__matrix[j][i]
                if i == self.__columns-1:
                    result += '\n'
        return result

    def __is_canvas_init(self):
        if self.__matrix \
                and self.__columns \
                and self.__rows:
            return True
        return False

    def __is_point_in_canvas(self, x, y):
        if not self.__is_canvas_init():
            raise Exception('canvas not init yet')
        if 0 < x < self.__columns and 0 < y < self.__rows:
            return True
        return False

    def add_line(self, x1, y1, x2, y2):
        if x1 != x2 and y1 != y2:
            raise Exception('not horizontal line or vertical line')
        if not self.__is_point_in_canvas(x1, y1) \
                or not self.__is_point_in_canvas(x2, y2):
            raise Exception('start and/or end point not in canvas')
        if x1 == x2:
            for r in range(y1, y2+1):
                self.__matrix[r][x1] = 'x'
        else:
            for c in range(x1, x2+1):
                self.__matrix[y1][c] = 'x'

    def add_rectangle(self, x1, y1, x2, y2):
        if x1 == x2 or y1 == y2:
            raise Exception('not rectangle')
        if not self.__is_point_in_canvas(x1, y1) \
                or not self.__is_point_in_canvas(x2, y2):
            raise Exception('start and/or end point not in canvas')
        for r in range(min(y1, y2), max(y1, y2) + 1):
            self.__matrix[r][min(x1, x2)] = 'x'
            self.__matrix[r][max(x1, x2)] = 'x'
        for c in range(min(x1, x2), max(x1, x2) + 1):
            self.__matrix[min(y1, y2)][c] = 'x'
            self.__matrix[max(y1, y2)][c] = 'x'

    def bucket_fill(self, x, y, c):
        if not self.__is_point_in_canvas(x, y):
            raise Exception('bucket fill start point not in canvas')
        queue = [(x, y)]
        visited = set()
        while len(queue) > 0:
            cell = queue.pop(0)
            if cell in visited or self.__matrix[cell[1]][cell[0]] in ['-', '|', 'x']:
                continue
            self.__matrix[cell[1]][cell[0]] = c
            visited.add(cell)
            if self.__is_point_in_canvas(cell[0]-1, cell[1]):
                queue.append((cell[0]-1, cell[1]))
            if self.__is_point_in_canvas(cell[0], cell[1]-1):
                queue.append((cell[0], cell[1]-1))
            if self.__is_point_in_canvas(cell[0]+1, cell[1]):
                queue.append((cell[0]+1, cell[1]))
            if self.__is_point_in_canvas(cell[0], cell[1]+1):
                queue.append((cell[0], cell[1]+1))

    def exit(self):
        sys.exit()
