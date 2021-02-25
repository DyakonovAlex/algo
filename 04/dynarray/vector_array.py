import ctypes

from dynamic_array import DynamicArray


class VectorArray(DynamicArray):

    __slots__ = ('actual_size', 'array', 'delta')

    def __init__(self):
        self.actual_size = 0
        self.delta = 1000
        self.array = self.make_array(0)

    def __len__(self) -> int:
        return self.actual_size

    def __getitem__(self, index: int):
        if not 0 <= index < self.actual_size:
            return IndexError(f"{index} is out of bounds!")

        return self.array[index]

    def size(self) -> int:
        return self.__len__()

    def empty(self) -> bool:
        return self.size() == 0

    def insert(self, item) -> None:
        if self.actual_size == len(self.array):
            self._resize(len(self.array) + self.delta)

        self.array[self.actual_size] = item
        self.actual_size += 1

    def insert_at(self, item, index: int) -> None:
        idx = index
        if idx < 0:
            idx = 0
        elif idx > self.actual_size:
            idx = self.actual_size

        if self.actual_size == len(self.array):
            self._resize(len(self.array) + self.delta)

        for i in range(self.actual_size - 1, idx - 1, -1):
            self.array[i + 1] = self.array[i]

        self.array[idx] = item
        self.actual_size += 1

    def delete(self):
        if self.actual_size == 0:
            return None
        item = self.array[self.actual_size - 1]
        self.array[self.actual_size - 1] = None
        self.actual_size -= 1
        return item

    def delete_at(self, index: int):
        if self.actual_size == 0:
            return None
        if index < 0 or index >= self.actual_size:
            return IndexError(f"{index} is out of bounds!")

        if index == self.actual_size - 1:
            return self.delete()

        item = self.array[index]

        for i in range(index, self.actual_size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.actual_size - 1] = None
        self.actual_size -= 1
        return item

    @staticmethod
    def make_array(capacity: int) -> ctypes.Array:
        """Возвращаем новый массив указанной емкости

        :param capacity: емкость
        :return: массив
        """
        return (capacity * ctypes.py_object)()

    def _resize(self, capacity: int) -> None:
        """Изменяем емкость внутреннего массива

        :param capacity: новая емкость
        :return: None
        """
        new_array = self.make_array(capacity)

        # for i in range(self.actual_count):
        #     new_array[i] = self.array[i]
        new_array[:-self.delta] = self.array[:]
        self.array = new_array
