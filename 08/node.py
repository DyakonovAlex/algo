from typing import Any


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
