import chessmen

from typing import Tuple


def moves(idx: int) -> Tuple[int, int]:
    """Прогулка Ладьи

    :param idx: Номер клетки
    :return: (Маска, количество_ходов)

    Одна из идей была найти строку и столбец
        row = idx // 8
        col = idx % 8
    и  использовать их, но не понятно, что я выигрываю.
    """
    start = 1 << idx

    left = (start >> 1) & chessmen.H
    right = (start << 1) & chessmen.A
    down = start >> 8
    up = start << 8
    for _ in range(6):
        left = (left | left >> 1) & chessmen.H
        right = (right | right << 1) & chessmen.A
        down = down | down >> 8
        up = up | up << 8

    result = (down | up | left | right) & chessmen.ALL_BORDER
    return result, chessmen.popcnt(result)


def main() -> None:
    mask: int
    cnt: int

    parser = chessmen.init_argparse()
    args = parser.parse_args()
    idx: int = args.index

    mask, cnt = moves(idx)

    print(cnt)
    print(mask)


if __name__ == '__main__':
    main()
