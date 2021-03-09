def merge_sort(arr: list, simulation: bool = False) -> None:
    def merge(left_idx: int, x: int, right_idx: int):
        arr_m = []
        a = left_idx
        b = x + 1

        if simulation:
            print("=" * 100)
            print(f"Merge: left index = {left_idx}, X = {x} and right index = {right_idx}", ":", *arr)

        while a <= x and b <= right_idx:
            if arr[a] < arr[b]:
                arr_m.append(arr[a])
                a += 1
            else:
                arr_m.append(arr[b])
                b += 1
            if simulation:
                print(f"{arr[a]} and {arr[b]}", ". array for merge:", *arr_m)

        while a <= x:
            arr_m.append(arr[a])
            a += 1
        while b <= right_idx:
            arr_m.append(arr[b])
            b += 1

        if simulation:
            print("array for merge:", *arr_m)

        for i in range(left_idx, right_idx + 1):
            arr[i] = arr_m[i - left_idx]

        if simulation:
            print("after merge:", *arr)

    def sort(left_idx: int, right_idx: int):
        if left_idx >= right_idx:
            return
        x = (left_idx + right_idx) // 2
        sort(left_idx, x)
        sort(x + 1, right_idx)
        merge(left_idx, x, right_idx)

    if simulation:
        print("begin sort array: ", *arr)

    sort(0, len(arr) - 1)

    if simulation:
        print("end sort array: ", *arr)


def main():
    array = [7, 0, 6, 1, 3, 2, 8, 5, 4, 9]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    merge_sort(array, simulation=True)
    print(*array)


if __name__ == '__main__':
    main()
