import ctypes

from dynamic_array import DynamicArray


class SingleArray(DynamicArray):

    __slots__ = ('array',)

    def __init__(self):
        self.array = self.make_array(0)

    def __len__(self) -> int:
        return len(self.array)

    def __getitem__(self, index: int):
        if not 0 <= index < len(self.array):
            return IndexError(f"{index} is out of bounds!")

        return self.array[index]

    def size(self) -> int:
        return self.__len__()

    def empty(self) -> bool:
        return self.size() == 0

    def insert(self, item) -> None:
        new_size = self.size() + 1
        self._resize(new_size)
        self.array[new_size - 1] = item

    def insert_at(self, item, index: int) -> None:
        idx = index
        if idx < 0:
            idx = 0
        elif idx > self.size():
            idx = self.size()

        new_size = self.size() + 1
        self._resize(new_size)

        for i in range(new_size-2, idx - 1, -1):
            self.array[i + 1] = self.array[i]

        self.array[idx] = item

    def delete(self):
        if self.size() == 0:
            return None
        item = self.array[self.size() - 1]
        self._resize(self.size() - 1)
        return item

    def delete_at(self, index: int):
        if self.size() == 0:
            return None
        if index < 0 or index >= self.size():
            return IndexError(f"{index} is out of bounds!")

        if index == self.size() - 1:
            return self.delete()

        item = self.array[index]

        for i in range(index, self.size() - 1):
            self.array[i] = self.array[i + 1]

        self._resize(self.size() - 1)
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

        # for i in range(self.size()):
        #     new_array[i] = self.array[i]
        if capacity < self.size():
            new_array[:] = self.array[:-1]
        else:
            new_array[:-1] = self.array[:]
        self.array = new_array
