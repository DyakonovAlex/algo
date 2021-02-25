import time

from dynamic_array import DynamicArray
from factor_array import FactorArray
from matrix_array import MatrixArray
from real_array import RealArray
from single_array import SingleArray
from vector_array import VectorArray

template = "|{:^20}|{:^20}|{:^50}|{:^50}|{:^50}|"


def testing(operation):
    def decorator(func):
        def wrapper(*args, **kwargs):
            global template
            arr = args[0]
            count = args[1]
            index = -1
            if len(args) == 3:
                index = args[2]

            class_name = type(arr).__name__
            start_time = time.time()
            func(*args, **kwargs)
            exec_time = (time.time() - start_time) * 1000
            print(template.format(class_name,
                                  count,
                                  operation + (' ' + str(index) if index >= 0 else ''),
                                  exec_time,
                                  exec_time * 1000 / count))

        return wrapper

    return decorator


def print_head():
    global template
    print(template.format("Class", "Count", "Operation", "Time (ms)", "Time per item (mks)"))
    print(template.format('-' * 18, '-' * 18, '-' * 48, '-' * 48, '-' * 48))


@testing("end insert")
def insert(array: DynamicArray, count: int) -> None:
    for i in range(count):
        array.insert(i)


@testing("insert at index")
def insert_at(array: DynamicArray, count: int, index: int) -> None:
    for i in range(count):
        array.insert_at(i, index)


@testing("end delete")
def delete(array: DynamicArray, count: int) -> None:
    for i in range(count):
        array.delete()


@testing("delete at index")
def delete_at(array: DynamicArray, count: int, index: int) -> None:
    for i in range(count):
        array.delete_at(index)


def main() -> None:
    global template

    count: int = 10_000
    real = RealArray()
    # single = SingleArray()
    vector = VectorArray()
    factor = FactorArray()
    matrix = MatrixArray()

    print_head()
    insert(real, count)
    # insert(single, count)
    insert(vector, count)
    insert(factor, count)
    insert(matrix, count)
    print(template.format('-' * 18, '-' * 18, '-' * 48, '-' * 48, '-' * 48))

    insert_at(real, count, count // 2)
    # insert_at(single, count, count // 2)
    insert_at(vector, count, count // 2)
    insert_at(factor, count, count // 2)
    insert_at(matrix, count, count // 2)
    print(template.format('-' * 18, '-' * 18, '-' * 48, '-' * 48, '-' * 48))

    insert_at(real, count, 0)
    # insert_at(single, count, 0)
    insert_at(vector, count, 0)
    insert_at(factor, count, 0)
    insert_at(matrix, count, 0)
    print(template.format('-' * 18, '-' * 18, '-' * 48, '-' * 48, '-' * 48))

    delete(real, count)
    # delete(single, count)
    delete(vector, count)
    delete(factor, count)
    delete(matrix, count)
    print(template.format('-' * 18, '-' * 18, '-' * 48, '-' * 48, '-' * 48))

    delete_at(real, count, count // 2)
    # delete_at(single, count, count // 2)
    delete_at(vector, count, count // 2)
    delete_at(factor, count, count // 2)
    delete_at(matrix, count, count // 2)
    print(template.format('-' * 18, '-' * 18, '-' * 48, '-' * 48, '-' * 48))

    for i in range(count):
        real.insert(i)
        # single.insert(i)
        vector.insert(i)
        matrix.insert(i)

    delete_at(real, count, 0)
    # delete_at(single, count, 0)
    delete_at(vector, count, 0)
    delete_at(factor, count, 0)
    delete_at(matrix, count, 0)
    print(template.format('-' * 18, '-' * 18, '-' * 48, '-' * 48, '-' * 48))


if __name__ == '__main__':
    main()
