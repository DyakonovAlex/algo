from countsort import counting_sort


def get_digit(number, n):
    return number // 10 ** n % 10


def radix_sort(arr: list, simulation: bool = False) -> None:
    for n in range(3):
        digit_arr = list(map(lambda num: get_digit(num, n), arr))
        items = list(zip(arr, digit_arr))
        counting_sort(items, simulation)
        for i, x in enumerate(items):
            arr[i] = x[0]


def main():
    array = [314, 301, 214, 221, 4]

    radix_sort(array, simulation=True)
    print("sorted:", *array)


if __name__ == '__main__':
    main()
