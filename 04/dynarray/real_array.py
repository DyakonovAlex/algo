from dynamic_array import DynamicArray


class RealArray(DynamicArray):
    __slots__ = ("array",)

    def __init__(self):
        self.array = list()

    def __len__(self) -> int:
        return self.array.__len__()

    def __getitem__(self, index: int):
        return self.array[index]

    def size(self) -> int:
        return self.__len__()

    def empty(self) -> bool:
        return self.size() == 0

    def insert(self, item) -> None:
        return self.array.append(item)

    def insert_at(self, item, index: int) -> None:
        return self.array.insert(index, item)

    def delete(self):
        return self.array.pop()

    def delete_at(self, index: int):
        return self.array.pop(index)
