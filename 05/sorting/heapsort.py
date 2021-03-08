import init
# from test.test_5 import get_arr


def heap_sort(arr: list, simulation: bool = False) -> None:
    def swap(a: int, b: int) -> None:
        arr[a], arr[b] = arr[b], arr[a]
        if simulation:
            print(f"swapped: {arr[a]} and {arr[b]}", ":", *arr)

    def heapify(root_idx: int, size: int) -> None:
        left_child = 2 * root_idx + 1
        right_child = left_child + 1
        max_idx = root_idx
        if left_child < size and arr[max_idx] < arr[left_child]:
            max_idx = left_child
        if right_child < size and arr[max_idx] < arr[right_child]:
            max_idx = right_child
        if max_idx == root_idx:
            return
        swap(max_idx, root_idx)
        heapify(max_idx, size)

    n = len(arr)

    if simulation:
        print("begin sort array: ", *arr)

    for root in range(n // 2 - 1, -1, -1):
        heapify(root, n)

    for j in range(n - 1, -1, -1):
        if simulation:
            print("=" * 100)
            print("j = ", j, ":", *arr)

        swap(0, j)
        heapify(0, j)

    if simulation:
        print("end sort array: ", *arr)


def main():
    array: list = init.get_array()
    # arr = [7, 0, 6, 1, 3, 2, 8, 5, 4, 9]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # array = arr
    # array = get_arr()
    heap_sort(array, simulation=False)
    init.print_result(array)


if __name__ == '__main__':
    main()
