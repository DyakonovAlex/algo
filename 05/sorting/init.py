import argparse


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Sorting array")
    parser.add_argument("len", type=int, help="Length array N >= 0")
    parser.add_argument("array", type=str, help="Array like 1,2,3,4,5")
    return parser


def get_array():
    parser = init_argparse()
    args = parser.parse_args()
    arr_len: int = args.len
    array: list = list(map(int, args.array.split(",")))
    return array


def print_result(arr):
    print(",".join(str(x) for x in arr))
