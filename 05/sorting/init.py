import argparse


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Sorting array")
    parser.add_argument("len", type=int, help="Length array N >= 0")
    parser.add_argument("array", type=str, help="Array like 1,2,3,4,5")
    return parser
