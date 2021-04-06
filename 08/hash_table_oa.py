from typing import Any, List, Final

INITIAL_CAPACITY: Final = 11
DEFAULT_LOAD_FACTOR: Final = 0.75


class Node:
    key: str
    value: Any
    _deleted: bool

    __slots__ = ("key", "value", "_deleted")

    def __init__(self, key: str, value: Any):
        self.key = key
        self.value = value
        self._deleted = False

    def __str__(self):
        return f"<Node: ({self.key}, {self.value}), deleted: {self._deleted}>"

    def __repr__(self):
        return str(self)

    @property
    def deleted(self):
        return self._deleted


class HashTableOA:

    capacity: int
    size: int
    threshold: int
    buckets: List[Node]

    __slots__ = ("capacity", "size", "buckets", "threshold")

    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.threshold = int(self.capacity * DEFAULT_LOAD_FACTOR)
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key: str) -> int:
        hashsum = 0
        for i, c in enumerate(key):
            hashsum += (i + len(key)) ** ord(c)
            hashsum %= 997
        return hashsum

    def put(self, key: str, value: Any, rehash: bool = False) -> None:
        hashed_value = self.hash(key)
        index = hashed_value % self.capacity
        node = self.buckets[index]

        while node is not None and not node.deleted and node.key != key:
            index = (index + 1) % self.capacity
            node = self.buckets[index]

        if node is not None and not node.deleted:
            node.value = value
            return

        if not rehash:
            self.size += 1
            if self.size > self.threshold:
                self.rehash()
                hashed_value = self.hash(key)
                index = hashed_value % self.capacity
                node = self.buckets[index]

                while node is not None:
                    index = (index + 1) % self.capacity
                    node = self.buckets[index]

        self.buckets[index] = Node(key, value)

    def get(self, key: str) -> Any:
        hashed_value = self.hash(key)
        index = hashed_value % self.capacity
        node = self.buckets[index]

        while node is not None and not node.deleted and node.key != key:
            index = (index + 1) % self.capacity
            node = self.buckets[index]

        if node is None or node.deleted:
            return None

        return node.value

    def del_(self, key: str) -> Any:
        hashed_value = self.hash(key)
        index = hashed_value % self.capacity
        node = self.buckets[index]

        while node is not None and not node.deleted and node.key != key:
            index = (index + 1) % self.capacity
            node = self.buckets[index]

        if node is None:
            return

        self.size -= 1
        node._deleted = True
        return node.value

    def rehash(self, debug=False) -> None:
        if debug:
            print("Before rehash")
            self.display()
            print("-" * 100)
        _buckets = [bucket for bucket in self.buckets if bucket is not None and not bucket.deleted]
        self.capacity *= 2
        self.threshold = int(self.capacity * DEFAULT_LOAD_FACTOR)
        self.buckets = [None] * self.capacity

        for node in _buckets:
            self.put(node.key, node.value, rehash=True)

        if debug:
            print("After rehash")
            self.display()
            print("-" * 100)
            print()

    def display(self):
        for i, node in enumerate(self.buckets):
            print(f"{i}:\t\t {node}")


def main():
    tbl = HashTableOA()
    arr = [i * 10 for i in range(1, 34)]
    print()
    print(*arr)
    print("-" * 100)
    for a in arr:
        tbl.put(str(a), a)

    print()
    tbl.display()

    print("-" * 100)
    print(f"get key = 30: {tbl.get('30')}")

    print("-" * 100)
    print(f"del key = 160: {tbl.del_('160')}")

    print("-" * 100)
    print(f"del key = 40: {tbl.del_('40')}")

    print("-" * 100)
    print(f"get key = 40: {tbl.get('40')}")

    print("-" * 100)
    print(f"add key = 40: {tbl.put('40',111)}")

    print("-" * 100)
    print(f"add key = 150: {tbl.put('150',111)}")

    print("-" * 100)
    print(f"get key = 40: {tbl.get('40')}")

    print()
    tbl.display()


if __name__ == '__main__':
    main()
