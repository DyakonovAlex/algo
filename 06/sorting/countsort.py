def counting_sort(items: list, simulation: bool = False) -> None:
    if simulation:
        print("begin sort array: ", *items)

    arr = [x[1] for x in items]
    k = 9
    counts = [0 for _ in range(k + 1)]
    for x in arr:
        counts[x] += 1
    if simulation:
        print("counts:", *counts)

    total = 0
    for i in range(k + 1):
        counts[i] += total
        total = counts[i]
    if simulation:
        print("total counts:", *counts)
        print("=" * 100)

    n = len(arr)
    outputs = [0 for _ in range(n)]
    for i, x in enumerate(arr[::-1]):
        tmp = counts[x] - 1
        outputs[tmp] = items[n - 1 - i]
        counts[x] -= 1
        if simulation:
            print(f"x = {x}, index in outputs = {counts[x]}", ":", *outputs)
            print("=" * 100)

    if simulation:
        print("end sort array: ", *outputs)
        print("=" * 100)
        print()

    items[:] = outputs[:]


def main():
    array = [2, 1, 0, 2, 7, 0, 1, 1, 3, 0, 8, 5]  # [7, 0, 6, 1, 3, 2, 8, 5, 4, 9] #
    key = [chr(x) for x in range(ord("a"), ord("l") + 1)]
    items = list(zip(key, array))

    counting_sort(items, simulation=True)
    print("sorted:", *items)


if __name__ == '__main__':
    main()
