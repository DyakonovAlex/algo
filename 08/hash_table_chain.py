from typing import Any, List, Final

from node import Node

INITIAL_CAPACITY: Final = 11
DEFAULT_LOAD_FACTOR: Final = 0.75


class HashTableChain:
    capacity: int
    size: int
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

    def put(self, key: str, value: Any, is_first: bool = True) -> None:
        index = self.hash(key)
        node = self.buckets[index]

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

        if is_first:
            _next = node
            node = Node(key, value)
            node.next = _next
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

    def rehash(self) -> None:
        _buckets = [bucket for bucket in self.buckets if bucket is not None]
        self.capacity *= 2
        self.threshold = int(self.capacity * DEFAULT_LOAD_FACTOR)
        self.buckets = [None] * self.capacity

        for bucket in _buckets:
            node = bucket
            while node is not None:
                self.put(node.key, node.value, False)
                node = node.next


def main():
    print("test")


if __name__ == '__main__':
    main()
