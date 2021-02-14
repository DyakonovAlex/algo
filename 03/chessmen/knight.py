import chessmen

from typing import Tuple


def moves(idx: int) -> Tuple[int, int]:
    """Прогулка Коня

    :param idx: Номер клетки
    :return: (Маска, количество_ходов)
    """
    start = 1 << idx

    result = (chessmen.GH & (start << 6 | start >> 10) |
              chessmen.H & (start << 15 | start >> 17) |
              chessmen.A & (start << 17 | start >> 15) |
              chessmen.AB & (start << 10 | start >> 6)) & chessmen.ALL_BORDER

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
