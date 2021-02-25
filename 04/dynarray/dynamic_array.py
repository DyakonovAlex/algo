from abc import ABCMeta, abstractmethod


class DynamicArray(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self) -> int:
        """
        :return: Количество элементов в массиве
        """
        pass

    @abstractmethod
    def __getitem__(self, index: int):
        """Возвращает элемент массива

        :param index: индекс элемента
        :return: элемент
        """
        pass

    @abstractmethod
    def size(self) -> int:
        """
        :return: Количество элементов в массиве
        """
        pass

    @abstractmethod
    def empty(self) -> bool:
        """Массив пустой?"""
        pass

    @abstractmethod
    def insert(self, item) -> None:
        """Добавляем элемент в конец массива

        :param item: элемент
        """
        pass

    @abstractmethod
    def insert_at(self, item, index: int) -> None:
        """Добавляем элемент в массив

        :param item: элемент
        :param index: индекс
        """
        pass

    @abstractmethod
    def delete(self):
        """Удаляем последний элемент из массива

        :return: удаленный элемент
        """
        pass

    @abstractmethod
    def delete_at(self, index: int):
        """Удаляем элемент по индексу

        :param index: индекс удаляемого элемента
        :return: удаленный элемент
        """
        pass
