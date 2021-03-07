import init


def _insertion_sort(arr: list, simulation: bool = False) -> None:
    """Classic"""

    n = len(arr)

    if simulation:
        print("begin sort array: ", *arr)

    for i in range(1, n):
        key = arr[i]
        if simulation:
            print("=" * 100)
            print("i = ", i, "key = ", key, ":", *arr)

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            if simulation:
                print(f"copy: arr[{j + 1}] = arr[{j}]", ":", *arr)
            j -= 1

        arr[j + 1] = key
        if simulation:
            print(f"copy: arr[{j + 1}] = {key}", ":", *arr)

    if simulation:
        print("end sort array: ", *arr)


def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid


def insertion_sort(arr: list, simulation: bool = False) -> list:
    """With binary search"""

    n = len(arr)

    if simulation:
        print("begin sort array: ", *arr)

    for i in range(1, n):
        key = arr[i]
        if simulation:
            print("=" * 100)
            print("i = ", i, "key = ", key, ":", *arr)

        j = binary_search(arr, key, 0, i - 1)
        if simulation:
            print("index found: ", j, ":", *arr)

        arr = arr[:j] + [key] + arr[j:i] + arr[i + 1:]
    return arr


def main():
    array: list = init.get_array()
    # arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # [7,0,6,1,3,2,8,5,4,9]
    # array = arr
    array = insertion_sort(array, simulation=False)
    init.print_result(array)


if __name__ == '__main__':
    main()
