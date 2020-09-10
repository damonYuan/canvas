#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))
from canvas import canvas


def handle(cmd, c):
    cmd_list = cmd.split()  # TODO: error handling, assume the input is valid
    if cmd_list[0] == 'C':
        c.init(*list(map(lambda x: int(x), cmd_list[1:])))
        print(c.draw())
    elif cmd_list[0] == 'L':
        c.add_line(*list(map(lambda x: int(x), cmd_list[1:])))
        print(c.draw())
    elif cmd_list[0] == 'R':
        c.add_rectangle(*list(map(lambda x: int(x), cmd_list[1:])))
        print(c.draw())
    elif cmd_list[0] == 'B':
        c.bucket_fill(int(cmd_list[1]), int(cmd_list[2]), cmd_list[3])
        print(c.draw())
        pass
    elif cmd_list[0] == 'Q':
        c.exit()
    else:
        raise Exception('Unknown command')


def main(): 
    c = canvas.Canvas()
    while True:
        cmd = input("enter command: ")
        try:
            handle(cmd, c)
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    main()
