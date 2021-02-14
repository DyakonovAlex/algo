import chessmen

from typing import Tuple


def moves(idx: int) -> Tuple[int, int]:
    """Прогулка Слона

    :param idx: Номер клетки
    :return: (Маска, количество_ходов)
    """
    start = 1 << idx

    up_left = (start << 7) & chessmen.H
    up_right = (start << 9) & chessmen.A
    down_left = (start >> 9) & chessmen.H
    down_right = (start >> 7) & chessmen.A
    for _ in range(6):
        up_left = (up_left | up_left << 7) & chessmen.H
        up_right = (up_right | up_right << 9) & chessmen.A
        down_left = (down_left | down_left >> 9) & chessmen.H
        down_right = (down_right | down_right >> 7) & chessmen.A

    result = (up_left | up_right | down_left | down_right) & chessmen.ALL_BORDER

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
