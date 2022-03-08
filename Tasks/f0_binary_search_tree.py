"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional
# import networkx as nx


# Пример как это выглядит:
# root = {
#     'key': 8,
#     'left': {
#         'key': 3,
#         'left': None,
#         'right': None
#     },
#     'right': {
#         'key': 10,
#         'left': None,
#         'right': {
#             'key': 14,
#             'left': None,
#             'right': None
#         }
#     }
# }

class BinarySearchTree:
    class Node:
        def __init__(self, key, value: Any, left=None, right=None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right

        def __str__(self):
            return f'({self.key}, {self.value})'

    def __init__(self):
        self.root = None   # Корень дерева

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree
        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """
        if self.root is None:
            self.root = self.Node(key, value)   # Если нет корня, то мы его создаем
        else:
            current_root = self.root
            while True:
                root_key = current_root.key
                if root_key == key:
                    current_root.value = value
                    break
                if key > root_key:
                    prev_root = current_root
                    current_root = current_root.right
                    if current_root is None:
                        prev_root.right = self.Node(key, value)
                        break
                else:
                    prev_root = current_root
                    current_root = current_root.left
                    if current_root is None:
                        prev_root.left = self.Node(key, value)
                        break

    def remove(self, key: int) -> Optional[str]:
        """
        Remove key and associated value from the BST if exists
        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        current_root = self.root

        if current_root is None:
            return None

        prev_root = None
        while True:
            root_key = current_root.key
            if root_key == key:
                break
            prev_root = current_root
            current_root = current_root.right if key > root_key else current_root.left

        del_root = current_root
        if prev_root is None:
            self.root = None
            return f'{del_root.key}, {del_root.value}'

        # 1. Если удаляемый элемент это лист
        if current_root.left is None and current_root.right is None:
            if prev_root.left == current_root:
                prev_root.left = None
                return f'{del_root.key}, {del_root.value}'
            else:
                prev_root.right = None
                return f'{del_root.key}, {del_root.value}'

        # 2. Если одного из детей нет, то удаляем узел и ставим вместо него существующего потомка
        elif current_root.left is None:
            if prev_root.left == current_root:
                prev_root.left = current_root.right
                return f'{del_root.key}, {del_root.value}'
            if prev_root.right == current_root:
                prev_root.right = current_root.right
                return f'{del_root.key}, {del_root.value}'
        elif current_root.right is None:
            if prev_root.left == current_root:
                prev_root.left = current_root.left
                return f'{del_root.key}, {del_root.value}'
            if prev_root.right == current_root:
                prev_root.right = current_root.left
                return f'{del_root.key}, {del_root.value}'

        # 3.
        else:
            del_root = current_root
            new_current_root = current_root.right
            while True:
                if new_current_root.left is None and new_current_root.right is None:
                    break
                new_current_root = new_current_root.left

            min_root = new_current_root
            current_root = min_root
            return f'{del_root.key}, {del_root.value}'

    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST
        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        current_root = self.root
        while True:
            root_key = current_root.key
            if root_key == key:
                print('Элемент найден')
                return current_root.value
            current_root = current_root.right if key > root_key else current_root.left
            if current_root is None:  # получаем лист(нет левого и правого)
                raise KeyError('Такого элемента нет')

    def clear(self) -> None:
        """
        Clear the tree
        :return: None
        """
        self.root = None
        return None


if __name__ == '__main__':
    root = BinarySearchTree()
    root.insert(14, 'b')
    print(root.root)
    root.insert(35, 'c')
    print(root.root.right)
    root.insert(31, 'd')
    print(root.root.right)
    root.insert(10, 'e')
    print(root.root.left)

