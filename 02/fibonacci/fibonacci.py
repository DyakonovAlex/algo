import argparse

from decimal import Decimal, getcontext, ROUND_FLOOR


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fibonacci number")
    parser.add_argument("num", type=int, help="Integer number N >= 0")
    return parser


def fib_very_bad(n: int) -> int:
    """Самый неудачный способ вычисления"""
    if n == 0 or n == 1:
        return n
    return fib_very_bad(n - 1) + fib_very_bad(n - 2)


def fib_iter(n: int) -> int:
    """Вычисление с помощью итераций"""
    if n == 0 or n == 1:
        return n

    f0: int = 0
    f1: int = 1
    f2: int = 1

    # 0,1,1,2,3,5,8,13,21,34,55
    for _ in range(1, n):
        f2 = f0 + f1
        f0 = f1
        f1 = f2

    return f2


def fib_formula(n: int) -> int:
    """По формуле золотого сечения"""
    if n == 0 or n == 1:
        return n

    getcontext().prec = n

    sqrt = Decimal(5).sqrt()
    phi = Decimal(1 + sqrt) / Decimal(2)

    res = phi ** Decimal(n) / sqrt + Decimal(1/2)

    return Decimal(res).quantize(Decimal('1.'), rounding=ROUND_FLOOR)


def multiply(matrix_a, matrix_b):
    matrix_c = []
    n = len(matrix_a)
    for i in range(n):
        list_1 = []
        for j in range(n):
            val = 0
            for k in range(n):
                val = val + matrix_a[i][k] * matrix_b[k][j]
            list_1.append(val)
        matrix_c.append(list_1)
    return matrix_c


def fib_matrix(n: int) -> int:
    """Через умножение матриц"""
    if n == 0 or n == 1:
        return n

    res_matrix = [[1, 0], [0, 1]]
    fibonacci_matrix = [[1, 1], [1, 0]]
    pwr = n - 1
    while pwr > 0:
        if pwr % 2 == 1:
            res_matrix = multiply(res_matrix, fibonacci_matrix)
        fibonacci_matrix = multiply(fibonacci_matrix, fibonacci_matrix)
        pwr //= 2

    return res_matrix[0][0]


def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    num: int = args.num

    # print(fib_iter(num))
    # print(fib_formula(num))
    print(fib_matrix(num))


if __name__ == '__main__':
    main()
