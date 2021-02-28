import init


def bubble_sort(arr: list) -> None:
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    parser = init.init_argparse()
    args = parser.parse_args()
    arr_len: int = args.len
    array: list = list(map(int, args.array.split(",")))
    bubble_sort(array)
    print(",".join(str(x) for x in array))


if __name__ == '__main__':
    main()
