import argparse
from typing import Final


A: Final = 0xfefefefefefefefe
H: Final = 0x7f7f7f7f7f7f7f7f
AB: Final = 0xFcFcFcFcFcFcFcFc
GH: Final = 0x3f3f3f3f3f3f3f3f
ALL_BORDER: Final = 0xffffffffffffffff


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Chessman's walk. "
                                                 "Print the number of possible chessman moves and bit mask moves")
    parser.add_argument("index", type=int, help="Index position 0 <= N <= 63")
    return parser


def popcnt(bits: int) -> int:
    """Считаем количество установленных битов

    :param bits: число
    :return: количество установленных битов
    """
    cnt: int = 0
    while bits > 0:
        cnt += 1
        bits &= (bits - 1)
    return cnt
