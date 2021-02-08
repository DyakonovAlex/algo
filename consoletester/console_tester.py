import argparse
import os
import re
import collections
import subprocess
import time


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Console Tester")
    parser.add_argument("prog_exec", type=str, help="Full path for program execute")
    parser.add_argument("test_dir", type=str, help="Full path to the test directory")
    return parser


def run_test(prog_exec: str, test_dir: str) -> None:
    # Example file name: test.2.out
    pattern_in = re.compile('(test)\.([0-9]+)\.(in)')
    pattern_out = re.compile('test\.[0-9]+\.out')

    data = {}
    expect = {}
    with os.scandir(test_dir) as entries:
        for entry in entries:
            if entry.is_file and (pattern_in.match(entry.name) or pattern_out.match(entry.name)):
                with open(os.path.join(test_dir, entry.name), 'r') as reader:
                    if pattern_in.match(entry.name):
                        data[entry.name.split('.')[1]] = reader.readlines()
                    elif pattern_out.match(entry.name):
                        expect[entry.name.split('.')[1]] = reader.readline().strip()

    data = collections.OrderedDict(sorted(data.items()))
    expect = collections.OrderedDict(sorted(expect.items()))

    print("Test:")
    for key, value in data.items():
        prm = ' '.join(map(lambda s: s.strip(), data[key]))
        # print("python", prog_exec, prm)
        start_time = time.time()
        actual = subprocess.run('python ' + prog_exec + ' ' + prm,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   text=True,
                                   shell=True)

        exec_time = (time.time() - start_time)

        if actual.stderr:
            print('Error:\n\t' + actual.stderr)

        if actual.stdout:
            print(f'{key}:\tTime: {exec_time} sec\tResult: {expect[key] == actual.stdout.strip()}\t{expect[key]} = {actual.stdout.strip()}')


def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    run_test(args.prog_exec, args.test_dir)


if __name__ == '__main__':
    main()
