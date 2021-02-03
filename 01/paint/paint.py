import curses
import time
import random

win_width: int
win_height: int
maps: list

symbols: list = ['', '#', '<', '>', '^', 'v', 'x']


def init_win(width: int, height: int):
    global win_width
    global win_height
    global maps

    win_width = width
    win_height = height
    maps = [['' for x in range(win_width)] for y in range(win_height)]

    curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    win = curses.newwin(win_height, win_width)
    curses.curs_set(0)
    win.border(0)
    return win


def terminate_win(win: any) -> None:
    curses.nocbreak()
    win.keypad(False)
    curses.echo()


def is_empty(x: int, y: int) -> bool:
    global win_width
    global win_height
    global maps

    if x < 1 or x >= win_width - 1:
        return False
    if y < 1 or y >= win_height - 1:
        return False

    return not maps[y][x]


def set_map(win: any, x: int, y: int, v: str, color_pair: int) -> None:
    global maps

    maps[y][x] = v
    win.addstr(y, x, v, curses.color_pair(color_pair))
    win.refresh()
    time.sleep(0.03)


# Рекурсивное заполнение
def fill(win: any, x: int, y: int, v: str) -> None:
    global symbols

    if not is_empty(x, y):
        return
    set_map(win, x, y, v, 2)
    fill(win, x - 1, y, symbols[2])
    fill(win, x + 1, y, symbols[3])
    fill(win, x, y - 1, symbols[4])
    fill(win, x, y + 1, symbols[5])
    set_map(win, x, y, symbols[6], 3)


# Алгоритм поиска вглубь
def fill_dfs(win: any, x: int, y: int) -> None:
    global symbols

    stack: list = [(x, y)]

    def push(a: int, b: int, v: str) -> None:
        if not is_empty(a, b):
            return
        set_map(win, a, b, v, 2)
        stack.append((a, b))

    if not is_empty(x, y):
        return

    while len(stack) > 0:
        x1, y1 = stack.pop()
        set_map(win, x1, y1, symbols[6], 3)
        push(x1 - 1, y1, symbols[2])
        push(x1 + 1, y1, symbols[3])
        push(x1, y1 - 1, symbols[4])
        push(x1, y1 + 1, symbols[5])


# Алгоритм поиска вширь
def fill_bfs(win: any, x: int, y: int) -> None:
    global symbols

    queue: list = [(x, y)]

    def push(a: int, b: int, v: str) -> None:
        if not is_empty(a, b):
            return
        set_map(win, a, b, v, 2)
        queue.append((a, b))

    if not is_empty(x, y):
        return

    while len(queue) > 0:
        x1, y1 = queue.pop(0)
        set_map(win, x1, y1, symbols[6], 3)
        push(x1 - 1, y1, symbols[2])
        push(x1 + 1, y1, symbols[3])
        push(x1, y1 - 1, symbols[4])
        push(x1, y1 + 1, symbols[5])


def add_random_pixels(win: any, cnt: int) -> None:
    global symbols

    for i in range(cnt + 1):
        set_map(win, random.randint(1, win_width - 2), random.randint(1, win_height - 2), '$', 1)


def main():
    global symbols

    try:
        win = init_win(50, 20)
        add_random_pixels(win, 300)
        win.refresh()
        # fill(win, 25, 10, symbols[1])
        # fill_dfs(win, 25, 10)
        fill_bfs(win, 25, 10)
        time.sleep(10)
    finally:
        terminate_win(win)


if __name__ == '__main__':
    main()
