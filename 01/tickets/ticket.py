import argparse
import math


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Number of Lucky tickets - Number of digits 2N")
    parser.add_argument("num_digit", type=int, help="Number (N)")
    return parser


#         9
# Nn(k) = ∑ Nn–1(k – i);
#         i=0
def num_var(n: int, k: int) -> int:
    nv: int = 0
    if n > 1:
        for i in range(10):
            nv += num_var(n - 1, k - i)
    else:
        nv += 1 if 0 <= k <= 9 else 0
    return nv


# Формула таже, только формируем массив для половины
# Для итога - возводим в квадрат
def lucky_tickets(num: int) -> int:
    if num <= 0:
        return 0
    array = [1] * 10 + [0] * (num * 9 - 9)

    for i in range(num - 1):
        array = [sum(array[x::-1]) if x < 10 else sum(array[x:x - 10:-1]) for x in range(len(array))]
    return sum([x ** 2 for x in array])


def lucky_tickets_6() -> int:
    cnt: int = 0
    for a1 in range(10):
        for a2 in range(10):
            for a3 in range(10):
                s123 = a1 + a2 + a3
                for b1 in range(10):
                    for b2 in range(10):
                        b3 = s123 - b1 - b2
                        if 0 <= b3 <= 9:
                            cnt += 1
    return cnt


n: int = 0
q: int = 0


def next_digit(nr: int, s1: int, s2: int) -> None:
    global n
    global q

    if nr == n:
        if s1 == s2:
            q += 1
        return

    for a in range(10):
        if nr < n / 2:
            next_digit(nr + 1, s1 + a, s2)
        else:
            next_digit(nr + 1, s1, s2 + a)


def lucky_ticket_rec(num: int) -> int:
    global n
    global q

    n = num
    q = 0
    next_digit(0, 0, 0)
    return q


def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    num_digit: int = args.num_digit

    # print(lucky_tickets_6())
    # print(lucky_ticket_rec(num_digit))
    # print(num_var(num_digit * 2, num_digit * 9))
    print(lucky_tickets(num_digit))


if __name__ == '__main__':
    main()
