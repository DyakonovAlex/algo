from typing import Any, List, Final


INITIAL_CAPACITY: Final = 11
DEFAULT_LOAD_FACTOR: Final = 0.75


class Node:
    __slots__ = ("key", "value", "next")

    def __init__(self, key: str, value: Any):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"<Node: ({self.key}, {self.value}), next: {self.next is not None}>"

    def __repr__(self):
        return str(self)


class HashTableChain:

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
            hashsum %= self.capacity
        return hashsum

    def put(self, key: str, value: Any, rehash: bool = False, first: bool = True) -> None:
        index = self.hash(key)
        node = self.buckets[index]

        if not rehash:
            # update
            _node = node
            while _node is not None and _node.key != key:
                _node = _node.next
            if _node is not None:
                _node.value = value
                return

            # insert
            self.size += 1
            if self.size > self.threshold:
                self.rehash()
                index = self.hash(key)
                node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            return

        if first:
            _next = node
            node = Node(key, value)
            node.next = _next
            self.buckets[index] = node
        else:
            _prev = node
            while node is not None:
                _prev = node
                node = node.next
            _prev.next = Node(key, value)

    def get(self, key: str) -> Any:
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None

        return node.value

    def del_(self, key: str) -> Any:
        index = self.hash(key)
        node = self.buckets[index]
        prev: Node = None
        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return

        self.size -= 1
        result = node.value
        if prev is None:
            self.buckets[index] = node.next
        else:
            prev.next = prev.next.next
        return result

    def rehash(self, debug=False) -> None:
        if debug:
            print("Before rehash")
            self.display()
            print("-" * 100)
        _buckets = [bucket for bucket in self.buckets if bucket is not None]
        self.capacity *= 2
        self.threshold = int(self.capacity * DEFAULT_LOAD_FACTOR)
        self.buckets = [None] * self.capacity

        for bucket in _buckets:
            node = bucket
            while node is not None:
                self.put(node.key, node.value, rehash=True, first=False)
                node = node.next

        if debug:
            print("After rehash")
            self.display()
            print("-" * 100)
            print()

    def display(self):
        for i, node in enumerate(self.buckets):
            print(f"{i}:\t\t", end="")
            _node = node
            while _node is not None:
                print(f"{_node.value} -> ", end="")
                _node = _node.next
            print()


def main():
    tbl = HashTableChain()
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

    print()
    tbl.display()


if __name__ == '__main__':
    main()
