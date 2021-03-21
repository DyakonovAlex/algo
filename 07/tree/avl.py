import logging

from typing import Optional, List

from node import Node


class AVL:
    __slots__ = ('root',)

    def __init__(self, *args):
        self.root = None

    def get_root(self) -> Node:
        return self.root

    def insert(self, key) -> None:
        if self.root:
            self._insert(self.root, key, None)
        else:
            self.root = Node(key)

    def _insert(self, node: Node, key: int, parent: Node) -> Node:
        if node is None:
            new = Node(key)
            new.parent = parent
            return new

        if key < node.key:
            node.left = self._insert(node.left, key, node)
        elif key > node.key:
            node.right = self._insert(node.right, key, node)

        # Step 2 - Update the height of the
        # ancestor node
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        # Step 3 - Get the balance factor
        node.bf = self.get_height(node.left) - self.get_height(node.right)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if node.bf > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Case 2 - Right Right
        if node.bf < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Case 3 - Left Right
        if node.bf > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Case 4 - Right Left
        if node.bf < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        print("=" * 100)
        self.get_root().display()

        # self._rebalance(node)
        return node

    def get_height(self, node: Node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def rebalance(self) -> None:
        self._rebalance(self.root)

    def _rebalance(self, node: Node) -> None:

        # Step 3 - Get the balance factor
        balance = self.get_balance(node)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.get_balance(node.left) >= 0:  # node.key < node.left.key:
            return self.right_rotate(node)

        # Case 2 - Right Right
        if balance < -1 and node.key > node.right.key:
            return self.left_rotate(node)

        # Case 3 - Left Right
        if balance > 1 and node.key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Case 4 - Right Left
        if balance < -1 and node.key < node.right.val:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def _update_height(self, node: Node) -> None:
        if node:
            l_h = node.left.height if node.left else 0
            r_h = node.right.height if node.right else 0
            node.height = 1 + max(l_h, r_h)
            self.update_heights(node.parent)

    def left_rotate(self, z) -> Node:

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z

        y.parent = z.parent
        z.parent = y
        if y.parent is None:
            self.root = y

        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        # Return the new root
        return y

    def right_rotate(self, z) -> Node:

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z

        y.parent = z.parent
        z.parent = y
        if y.parent is None:
            self.root = y

        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
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
    avl = AVL()

    arr = [20, 10, 30, 4, 16, 7, 5]  # , 8, 14, 18, 11, 12]
    for x in arr:
        avl.insert(x)

    print("=" * 100)
    avl.get_root().display()

    print("=" * 100)
    print("in order:", *avl.inorder())

    print("=" * 100)
    print("search 16:", avl.search(16))
    print("search 40:", avl.search(43))

    # print("=" * 100)
    # print("delete 10")
    # avl.remove(10)
    # print("in order:", *avl.inorder())


if __name__ == '__main__':
    main()
