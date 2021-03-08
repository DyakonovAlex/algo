import init
# from test.test_5 import get_arr


def gaps_classic(n: int):
    def gap():
        g = n
        while g > 0:
            g //= 2
            yield g

    result = []
    for g in gap():
        result.append(g)

    result = result[::-1]
    return result


def gaps_1(n: int):
    def gap():
        k = -1
        while True:
            g = (2 ** k) + 1
            k += 1
            yield int(g)

    result = [0]
    for g in gap():
        if g < n:
            result.append(g)
        else:
            break

    return result


def gaps_2(n: int) -> int:
    def gap():
        k = 1
        while True:
            g = (4 ** k) + (3 * 2 ** (k - 1)) + 1
            k += 1
            yield int(g)

    result = [0, 1]
    for g in gap():
        if g < n:
            result.append(g)
        else:
            break

    return result


def shell_sort(arr: list, list_gap, simulation: bool = False) -> None:
    n = len(arr)
    gaps = list_gap(n)

    if simulation:
        print("begin sort array: ", *arr)

    # while gap > 0:
    for gap in gaps[::-1]:
        if simulation:
            print("gap = ", gap, ": ", *arr)

        for i in range(gap, n):
            key = arr[i]
            if simulation:
                print("=" * 100)
                print("i = ", i, "key = ", key, ":", *arr)

            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                if simulation:
                    print(f"copy: arr[{j}] = arr[{j - gap}]", ":", *arr)
                j -= gap

            arr[j] = key
            if simulation:
                print(f"copy: arr[{j}] = {key}", ":", *arr)

        # gap = func_gap(gap)

    if simulation:
        print("end sort array: ", *arr)


def main():
    array: list = init.get_array()
    # arr = [7, 0, 6, 1, 3, 2, 8, 5, 4, 9]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # array = arr
    # array = get_arr()
    shell_sort(array, gaps_classic, simulation=False)
    # shell_sort(array, gaps_1, simulation=False)
    # shell_sort(array, gaps_2, simulation=False)
    init.print_result(array)


if __name__ == '__main__':
    main()
