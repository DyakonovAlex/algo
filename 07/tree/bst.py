import logging

from typing import Optional, List

from node import Node


class BST:
    __slots__ = ('root',)

    def __init__(self):
        self.root = None

    def get_root(self) -> Node:
        return self.root

    def insert(self, key) -> None:
        if self.root:
            self._insert(self.root, key)
        else:
            self.root = Node(key)

    def _insert(self, node: Node, key: int) -> Node:
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def search(self, key) -> Node:
        return self._search(self.root, key)

    def _search(self, node: Node, key: int) -> Optional[Node]:
        if node is None or node.key == key:
            return node

        if key < node.key:
            node = self._search(node.left, key)
        else:
            node = self._search(node.right, key)
        return node

    def remove(self, key: int) -> None:
        if self.root:
            self._remove(self.root, key)

    def _remove(self, node: Node, key: int) -> Optional[Node]:
        if not node:
            return None

        if node.key == key:
            if node.left:
                left_right_most = node.left
                while left_right_most.right:
                    left_right_most = left_right_most.right
                node.left = self._remove(node.left, left_right_most.key)
                left_right_most.right = node.right
                left_right_most.left = node.left
                return left_right_most
            else:
                return node.right
        elif key < node.key:
            node.left = self._remove(node.left, key)
        else:
            node.right = self._remove(node.right, key)
        return node

    def inorder(self) -> List[int]:
        return self._inorder(self.root)

    def _inorder(self, node) -> List[int]:
        arr = []
        if node:
            arr = self._inorder(node.left)
            arr.append(node.key)
            arr = arr + self._inorder(node.right)
        return arr


def main():
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

    bst = BST()
    arr = [20, 10, 30, 4, 16, 7, 5, 8, 14, 18, 11, 12]
    for x in arr:
        bst.insert(x)

    print("=" * 100)
    bst.get_root().display()

    print("=" * 100)
    print("in order:", *bst.inorder())

    print("=" * 100)
    print("search 16:", bst.search(16))
    print("search 40:", bst.search(43))

    print("=" * 100)
    print("delete 10")
    bst.remove(10)
    print("in order:", *bst.inorder())

    print("=" * 100)
    bst.get_root().display()


if __name__ == '__main__':
    main()
