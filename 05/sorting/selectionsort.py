import init


def selection_sort(arr: list, simulation: bool = False) -> None:
    def swap(a: int, b: int) -> None:
        arr[a], arr[b] = arr[b], arr[a]
        if simulation:
            print(f"swapped: {arr[a]} and {arr[b]}", ":", *arr)

    def move_max_to_root(root: int, size: int) -> None:
        for i in range(root + 1, size):
            if arr[root] < arr[i]:
                swap(root, i)
        pass

    n = len(arr)

    if simulation:
        print("begin sort array: ", *arr)

    move_max_to_root(0, n)
    for j in range(n - 1, -1, -1):
        if simulation:
            print("=" * 100)
            print("j = ", j, ":", *arr)

        swap(0, j)
        move_max_to_root(0, j)

    if simulation:
        print("end sort array: ", *arr)


def main():
    array: list = init.get_array()
    # arr = [7, 0, 6, 1, 3, 2, 8, 5, 4, 9]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # array = arr
    selection_sort(array, simulation=False)
    init.print_result(array)


if __name__ == '__main__':
    main()
