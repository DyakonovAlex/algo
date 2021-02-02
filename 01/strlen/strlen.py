import argparse


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(usage="%(prog)s STRING", description="Print string length")
    parser.add_argument("str", type=str, help="String")
    return parser


def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    if args.str:
        print(len(args.str))
    else:
        print(0)


if __name__ == '__main__':
    main()
