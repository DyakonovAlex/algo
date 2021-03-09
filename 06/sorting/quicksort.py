def quick_sort(arr: list, simulation: bool = False) -> None:
    def swap(a: int, b: int) -> None:
        arr[a], arr[b] = arr[b], arr[a]
        if simulation:
            print(f"swapped: {arr[a]} and {arr[b]}", ":", *arr)

    def split(left_idx: int, right_idx: int) -> int:
        pivot = arr[right_idx]
        a = left_idx - 1
        if simulation:
            print(f"pivot = {pivot}, a = {a}, left index = {left_idx}, right index = {right_idx}")
        for m in range(left_idx, right_idx + 1):
            if arr[m] <= pivot:
                a += 1
                swap(a, m)
        return a

    def sort(left_idx: int, right_idx: int):
        if left_idx >= right_idx:
            return
        x = split(left_idx, right_idx)
        sort(left_idx, x - 1)
        sort(x + 1, right_idx)

    if simulation:
        print("begin sort array: ", *arr)

    sort(0, len(arr) - 1)

    if simulation:
        print("end sort array: ", *arr)


def main():
    array = [7, 0, 6, 1, 3, 2, 8, 5, 4, 9]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    quick_sort(array, simulation=False)
    print(*array)


if __name__ == '__main__':
    main()
