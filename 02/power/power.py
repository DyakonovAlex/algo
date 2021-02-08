import argparse

from typing import List


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Raise number to a power")
    parser.add_argument("real_num", type=float, help="Real number")
    parser.add_argument("pwr", type=int, help="Power")
    return parser


def power_iter(a: float, n: int) -> float:
    """Итеративное возведение в степень"""
    if n == 0:
        return 1

    p: float = a
    for _ in range(1, n):
        p *= a
    return p


def power_two(a: float, n: int) -> float:
    """Возведение в степень через степень двойки
    с домножением"""
    if n == 0:
        return 1

    i: int = 1
    p: float = a
    while i * 2 <= n:
        p *= p
        i *= 2

    for _ in range(n - i):
        p *= a

    return p


def power_decomp(a: float, n: int) -> float:
    """Возведение в степень через двоичное разложение
    показателя степени"""
    if n == 0:
        return 1

    i: int = 1
    p: float = a
    plist: List[float] = [a]
    d: int = n
    lst: List[int] = [n % 2]
    while i * 2 <= n:
        p *= p
        i *= 2
        d //= 2
        lst.append(d % 2)
        plist.append(p)

    result: float = 1
    for count, value in enumerate(lst):
        if value == 1:
            result *= plist[count]

    return result


def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    real_num: float = args.real_num
    pwr: int = args.pwr

    # print(format(power_iter(real_num, pwr), '.11f'))
    # print(format(power_two(real_num, pwr), '.11f'))
    print(format(power_decomp(real_num, pwr), '.11f'))


if __name__ == '__main__':
    main()
