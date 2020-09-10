#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))
from canvas import canvas


class TestCanvas:

    def test_passed_init(self):
        c = canvas.Canvas()
        c.init(20, 4)
        assert c.draw() == '----------------------\n' \
                           '|                    |\n' \
                           '|                    |\n' \
                           '|                    |\n' \
                           '|                    |\n' \
                           '----------------------\n'

    def test_failed_without_init(self):
        try:
            c = canvas.Canvas()
            c.add_line(1, 2, 6, 2)
        except Exception as e:
            assert str(e) == 'canvas not init yet'

    def test_passed_add_line(self):
        c = canvas.Canvas()
        c.init(20, 4)
        c.add_line(1, 2, 6, 2)
        assert c.draw() == '----------------------\n' \
                           '|                    |\n' \
                           '|xxxxxx              |\n' \
                           '|                    |\n' \
                           '|                    |\n' \
                           '----------------------\n'

    def test_failed_add_line(self):
        try:
            c = canvas.Canvas()
            c.init(20, 4)
            c.add_line(1, 2, 6, 3)
            assert False
        except Exception as e:
            assert str(e) == 'not horizontal line or vertical line'

        try:
            c = canvas.Canvas()
            c.init(20, 4)
            c.add_line(1, 100, 6, 100)
        except Exception as e:
            assert str(e) == 'start and/or end point not in canvas'

    def test_passed_add_rectangle(self):
        c = canvas.Canvas()
        c.init(20, 4)
        c.add_rectangle(14, 1, 18, 3)
        assert c.draw() == '----------------------\n' \
                           '|             xxxxx  |\n' \
                           '|             x   x  |\n' \
                           '|             xxxxx  |\n' \
                           '|                    |\n' \
                           '----------------------\n'

    def test_failed_add_rectangle(self):
        try:
            c = canvas.Canvas()
            c.init(20, 4)
            c.add_rectangle(14, 1, 18, 1)
        except Exception as e:
            assert str(e) == 'not rectangle'

        try:
            c = canvas.Canvas()
            c.init(20, 4)
            c.add_rectangle(14, 1, 18, 100)
        except Exception as e:
            assert str(e) == 'start and/or end point not in canvas'

    def test_passed_bucket_fill(self):
        c = canvas.Canvas()
        c.init(20, 4)
        c.add_rectangle(14, 1, 18, 3)
        c.bucket_fill(15, 2, 'o')
        assert c.draw() == '----------------------\n' \
                           '|             xxxxx  |\n' \
                           '|             xooox  |\n' \
                           '|             xxxxx  |\n' \
                           '|                    |\n' \
                           '----------------------\n'

    def test_failed_bucket_fill(self):
        try:
            c = canvas.Canvas()
            c.init(20, 4)
            c.add_rectangle(14, 1, 18, 100)
            c.bucket_fill(100, 2, 'o')
        except Exception as e:
            assert str(e) == 'start and/or end point not in canvas'

    def test_passed_generic(self):
        c = canvas.Canvas()
        c.init(20, 4)
        c.add_line(1, 2, 6, 2)
        c.add_line(6, 3, 6, 4)
        c.add_rectangle(14, 1, 18, 3)
        c.bucket_fill(10, 3, 'o')
        assert c.draw() == '----------------------\n' \
                           '|oooooooooooooxxxxxoo|\n' \
                           '|xxxxxxooooooox   xoo|\n' \
                           '|     xoooooooxxxxxoo|\n' \
                           '|     xoooooooooooooo|\n' \
                           '----------------------\n'
        c.bucket_fill(10, 3, 'c')
        assert c.draw() == '----------------------\n' \
                           '|cccccccccccccxxxxxcc|\n' \
                           '|xxxxxxcccccccx   xcc|\n' \
                           '|     xcccccccxxxxxcc|\n' \
                           '|     xcccccccccccccc|\n' \
                           '----------------------\n'
        c.bucket_fill(1, 3, 'a')
        assert c.draw() == '----------------------\n' \
                           '|cccccccccccccxxxxxcc|\n' \
                           '|xxxxxxcccccccx   xcc|\n' \
                           '|aaaaaxcccccccxxxxxcc|\n' \
                           '|aaaaaxcccccccccccccc|\n' \
                           '----------------------\n'


