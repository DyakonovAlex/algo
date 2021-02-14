import chessmen

from typing import Tuple


def moves(idx: int) -> Tuple[int, int]:
    """Прогулка Короля

    :param idx: Номер клетки
    :return: (Маска, количество_ходов)
    """
    k = 1 << idx
    ka = k & chessmen.A
    kh = k & chessmen.H

    result = (ka << 7 | k << 8 | kh << 9 |
              ka >> 1 | kh << 1 |
              ka >> 9 | k >> 8 | kh >> 7) & chessmen.ALL_BORDER
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
