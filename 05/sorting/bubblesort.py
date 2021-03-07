import init


def bubble_sort(arr: list, simulation: bool = False) -> None:
    swapped = True
    last_index = len(arr) - 1

    if simulation:
        print("begin sort array: ", *arr)

    while swapped:
        swapped = False
        if simulation:
            print("=" * 100)
        n = last_index
        for i in range(n):
            if simulation:
                print("i = ", i, "last index", last_index, ":", *arr)

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                last_index = i
                if simulation:
                    print("swapped", "last index", last_index, ":", *arr)

    if simulation:
        print("end sort array: ", *arr)


def main():
    array: list = init.get_array()
    bubble_sort(array, simulation=False)
    init.print_result(array)


if __name__ == '__main__':
    main()
