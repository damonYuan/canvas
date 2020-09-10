#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))
from canvas import app


class MockedCanvas:
    def __init__(self):
        self.exit_called = False
        self.c = None
        self.l = None
        self.r = None
        self.b = None

    def init(self, width, height):
        self.c = (width, height)

    def draw(self):
        return "mock"

    def add_line(self, x1, y1, x2, y2):
        self.l = (x1, y1, x2, y2)

    def add_rectangle(self, x1, y1, x2, y2):
        self.r = (x1, y1, x2, y2)

    def bucket_fill(self, x, y, c):
        self.b = (x, y, c)

    def exit(self):
        self.exit_called = True


mock = MockedCanvas()


def test_passed_with_c():
    app.handle('C 20 4', mock)
    assert mock.c == (20, 4)


def test_passed_with_l():
    app.handle('L 1 2 6 2', mock)
    assert mock.l == (1, 2, 6, 2)


def test_passed_with_r():
    app.handle('R 14 1 18 3', mock)
    assert mock.r == (14, 1, 18, 3)


def test_passed_with_b():
    app.handle('B 10 3 o', mock)
    assert mock.b == (10, 3, 'o')


def test_passed_with_q():
    app.handle('Q', mock)
    assert mock.exit_called is True


def test_failed_with_random():
    try:
        app.handle('asda', mock)
        assert False
    except Exception as e:
        assert str(e) == 'Unknown command'


