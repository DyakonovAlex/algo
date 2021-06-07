import argparse
import os


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Zip / Unzip file")
    parser.add_argument("action", type=str, help="zip or unzip")
    parser.add_argument("src_name", type=str, help="source file name")
    parser.add_argument("dst_name", type=str, help="destination file name")
    return parser


def length_sequence(chr: str, seq: str, start: int, end: int):
    n = start
    result: int = 0
    while n < end and chr == seq[n]:
        result += 1
        n += 1
    return result


def zip_sequence(seq: str) -> list:
    def add_bytes(count_char: int, chars: str):
        bt = count_char.to_bytes(1, byteorder='big', signed=True)
        ch = chars.encode('utf-8')
        result.append(bt)
        result.append(ch)

    result: list = []
    n = 0
    seq_len = len(seq)
    cnt_diff: int = 0
    while n + 1 <= seq_len:
        cnt = length_sequence(seq[n], seq, n + 1, seq_len) + 1
        if cnt > 1:
            if cnt_diff > 0:
                add_bytes(-cnt_diff, seq[n - cnt_diff:n])
            add_bytes(cnt, seq[n])
            cnt_diff = 0
        else:
            cnt_diff += 1
        n += cnt
    if cnt_diff > 0:
        add_bytes(-cnt_diff, seq[n - cnt_diff:n])
    return result


def zip_file(file_name: str, zip_file_name: str):
    with open(file_name, "r") as reader, open(zip_file_name, 'wb') as writer:
        for line in reader.readlines():
            for z in zip_sequence(line):
                writer.write(bytes(z))


def unzip_file(zip_file_name: str, unzip_file_name: str):
    def get_sequence(seek: int, seq_len: int) -> str:
        reader.seek(seek)
        byte = reader.read(1)
        ch = byte.decode("utf-8")
        return ch * seq_len

    result: str = ""
    with open(zip_file_name, "rb") as reader, open(unzip_file_name, "w") as writer:
        n = 0
        end = os.path.getsize(zip_file_name)

        while n < end:
            reader.seek(n)
            byte = reader.read(1)
            cnt = int.from_bytes(byte, byteorder='big', signed=True)
            if cnt > 0:
                result += get_sequence(n + 1, cnt)
                n += 2
            else:
                for i in range(-cnt):
                    result += get_sequence(n + 1, 1)
                    n += 1
                n += 1
            if len(result) > 500:
                writer.write(result)
                result = ""
        writer.write(result)


def main():
    parser = init_argparse()
    args = parser.parse_args()
    action: str = args.action
    src_name: str = args.src_name
    dst_name: str = args.dst_name

    if action == "zip":
        zip_file(src_name, dst_name)
    elif action == "unzip":
        unzip_file(src_name, dst_name)
    else:
        print("unknown action")


if __name__ == "__main__":
    main()
