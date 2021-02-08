import argparse

from decimal import Decimal, ROUND_HALF_UP


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Raise number to a power")
    parser.add_argument("real_num", type=float, help="Real number")
    parser.add_argument("pwr", type=int, help="Power")
    return parser


def power_iter(a: Decimal, n: int) -> Decimal:
    """Итеративное возведение в степень"""
    if n == 0:
        return 1.0

    a = Decimal(a)
    p: Decimal = a
    for _ in range(1, n):
        p = Decimal(p * a)

    return Decimal(p).quantize(Decimal('.00000000001'), rounding=ROUND_HALF_UP)


def power_two(a: Decimal, n: int) -> Decimal:
    """Возведение в степень через степень двойки
    с домножением"""
    if n == 0:
        return 1.0

    i: int = 1
    a = Decimal(a)
    p: Decimal = a
    while i * 2 <= n:
        p = Decimal(p * p)
        i *= 2

    for _ in range(n - i):
        p = Decimal(p * a)

    return Decimal(p).quantize(Decimal('.00000000001'), rounding=ROUND_HALF_UP)


def power_decomp(a: Decimal, n: int) -> Decimal:
    """Возведение в степень через двоичное разложение
    показателя степени"""
    if n == 0:
        return 1.0

    base: Decimal = Decimal(a)
    pwr: int = n
    res: Decimal = Decimal(1)
    while pwr > 1:
        if pwr % 2 == 1:
            res = Decimal(res * base)

        base = Decimal(base * base)
        pwr //= 2

    if pwr > 0:
        res = Decimal(res * base)

    return Decimal(res).quantize(Decimal('.00000000001'), rounding=ROUND_HALF_UP)


def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    real_num: float = args.real_num
    pwr: int = args.pwr

    print(power_decomp(real_num, pwr))
    # print(power_two(real_num, pwr))
    # print(power_iter(real_num, pwr))


if __name__ == '__main__':
    main()
