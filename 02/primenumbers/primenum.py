import argparse
import math

from typing import List


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Count of prime numbers")
    parser.add_argument("num", type=int, help="Integer number N >= 1")
    return parser


primes: List[int]
count: int


def is_prime(num: int) -> bool:
    global primes

    if num == 2:
        return True
    if num % 2 == 0:
        return False

    i: int = 0
    sqrt: int = int(math.sqrt(num))
    while primes[i] <= sqrt:
        if num % primes[i] == 0:
            return False
        i += 1
    return True


def count_primes(num: int) -> int:
    """Перебор делителей, с использованием массива"""

    global count
    global primes

    if num == 1:
        return 0

    count = 1
    primes = [2]
    p: int = 3
    while p <= num:
        if is_prime(p):
            count += 1
            primes.append(p)
        p += 2
    return count


def eratosthen_1(num: int) -> int:
    """Решето Эратосфена со сложностью O(n log log n)"""

    if num == 1:
        return 0

    divs: List[bool] = [False for _ in range(num + 1)]
    cnt: int = 0
    for p in range(2, num + 1):
        if not divs[p]:
            cnt += 1
            for j in range(p * p, num + 1, p):
                divs[j] = True
        p += 1

    return cnt


def eratosthen_2(num: int) -> int:
    """Решето Эратосфена со сложностью O(n log log n)
    Фомируем множество непростых чисел"""

    if num == 1:
        return 0

    not_primes: set = set()
    cnt: int = 0
    for p in range(2, num + 1):
        if p in not_primes:
            continue

        cnt += 1
        not_primes.update(range(p * p, num + 1, p))
    return cnt


def eratosthen_3(num: int) -> int:
    """Решето Эратосфена со сложностью O(n)"""

    if num == 1:
        return 0

    lp: List[int] = [0 for _ in range(num + 1)]
    pr: list = list()
    cnt: int = 0

    for i in range(2, num + 1):
        if lp[i] == 0:
            lp[i] = i
            cnt += 1
            pr.append(i)
        j = 0
        while j < cnt and pr[j] <= lp[i] and i * pr[j] <= num:
            lp[i * pr[j]] = pr[j]
            j += 1
    return cnt


def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    num: int = args.num

    # print(count_primes(num))
    print(eratosthen_3(num))


if __name__ == '__main__':
    main()
