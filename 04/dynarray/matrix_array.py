import ctypes

from dynamic_array import DynamicArray


class MatrixArray(DynamicArray):
    __slots__ = ('actual_size', 'total_row', 'total_column', 'array')

    def __init__(self):
        self.actual_size = 0
        self.total_row = 1
        self.total_column = 1000
        self.array = self.make_matrix(self.total_row, self.total_column)

    def __len__(self) -> int:
        return self.actual_size

    def __getitem__(self, index: int):
        if not 0 <= index < self.actual_size:
            return IndexError(f"{index} is out of bounds!")

        row = self.get_row(index)
        column = self.get_column(index)
        return self.array[row][column]

    def __setitem__(self, index, value):
        if not 0 <= index < self.actual_size:
            return IndexError(f"{index} is out of bounds!")

        row = self.get_row(index)
        column = self.get_column(index)
        self.array[row][column] = value

    def size(self) -> int:
        return self.__len__()

    def empty(self) -> bool:
        return self.size() == 0

    def insert(self, item) -> None:
        if self.actual_size == self.total_row * self.total_column:
            self._resize(self.total_row + 1)

        row = self.get_row(self.actual_size)
        column = self.get_column(self.actual_size)
        self.array[row][column] = item
        self.actual_size += 1

    def get_row(self, index):
        return index // self.total_column

    def get_column(self, index):
        return index % self.total_column

    def insert_at(self, item, index: int) -> None:
        idx = index
        if idx < 0:
            idx = 0
        elif idx > self.actual_size:
            idx = self.actual_size

        if self.actual_size == self.total_row * self.total_column:
            self._resize(self.total_row + 1)

        self.actual_size += 1
        for i in range(self.actual_size - 2, idx - 1, -1):
            self[i + 1] = self[i]

        self[idx] = item

    def delete(self):
        if self.actual_size == 0:
            return None

        row = self.get_row(self.actual_size - 1)
        column = self.get_column(self.actual_size - 1)
        item = self.array[row][column]
        self.array[row][column] = None
        self.actual_size -= 1
        return item

    def delete_at(self, index: int):
        if self.actual_size == 0:
            return None
        if index < 0 or index >= self.actual_size:
            return IndexError(f"{index} is out of bounds!")

        if index == self.actual_size - 1:
            return self.delete()

        item = self[index]

        for i in range(index, self.actual_size - 1):
            self[i] = self[i + 1]

        self[self.actual_size - 1] = None
        self.actual_size -= 1
        return item

    @staticmethod
    def make_matrix(row: int, column: int) -> ctypes.Array:
        """Создаем матрицу указанного размера

        :param row: количество строк
        :param column: количество колоное
        :return: матрица
        """
        return ((column * ctypes.py_object) * row)()

    def _resize(self, row: int) -> None:
        """ Устанавливаем новое количество строк в матрице

        :param row: количество строк
        :return:
        """
        new_array = self.make_matrix(row, self.total_column)

        new_array[:-1] = self.array[:]
        self.array = new_array
        self.total_row += 1
