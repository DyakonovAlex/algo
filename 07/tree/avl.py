import functools

from typing import Optional, List

from node import Node


class AVL:
    __slots__ = ('root',)

    def debug(func):
        @functools.wraps(func)
        def wrapper_debug(*args):
            args_repr = [repr(a) for a in args[1:]]
            signature = ", ".join(args_repr)
            print(f"Befor calling {func.__name__}({signature})")
            args[0].get_root().display()
            print()
            value = func(*args)
            print(f"After calling {func.__name__}({signature})")
            args[0].get_root().display()
            print()
            print("-" * 100)
            print()
            return value

        return wrapper_debug

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

        node = self.rebalance(node)

        return node

    @staticmethod
    def get_height(node: Node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def rebalance(self, node: Node) -> Node:

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        bf = self.get_balance(node)

        # Case 1 - Left Left
        if bf > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

            # Case 2 - Right Right
        if bf < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

            # Case 3 - Left Right
        if bf > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

            # Case 4 - Right Left
        if bf < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def left_rotate(self, node) -> Node:

        y = node.right
        y_left = y.left

        # Perform rotation
        y.left = node

        # Check node is root
        if self.get_root() == node:
            self.root = y

        node.right = y_left

        # Update heights
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y

    def right_rotate(self, node) -> Node:

        y = node.left
        y_right = y.right

        # Perform rotation
        y.right = node

        # Check node is root
        if self.get_root() == node:
            self.root = y

        node.left = y_right

        # Update heights
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        # Return the new root
        return y

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
                left_right_most = self.rebalance(left_right_most)
                return left_right_most
            else:
                return node.right
        elif key < node.key:
            node.left = self._remove(node.left, key)
        else:
            node.right = self._remove(node.right, key)

        node = self.rebalance(node)

        return node

    def inorder(self) -> List[str]:
        return self._inorder(self.root)

    def _inorder(self, node) -> List[str]:
        arr: List[str] = []
        if node:
            arr = self._inorder(node.left)
            arr.append(f"{node.key} - {node.height}")
            arr = arr + self._inorder(node.right)
        return arr


def main():
    avl = AVL()

    arr = [20, 10, 30, 4, 16, 7, 5, 8, 14, 18, 11, 12]
    for x in arr:
        avl.insert(x)
        # print()
        # print(f"Added {x}")
        # print()
        # avl.get_root().display()
        # print("=" * 100)

    print("=" * 100)
    print("in order:", *avl.inorder())

    print("=" * 100)
    print("search 16:", avl.search(16))
    print("search 40:", avl.search(43))

    print("=" * 100)
    avl.remove(5)
    print("in order:", *avl.inorder())

    print("=" * 100)
    avl.get_root().display()


if __name__ == '__main__':
    main()
