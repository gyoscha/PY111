"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
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
    class Node:   # ToDo Попробовать заменить словарь (create_node) на класс Node
        def __init__(self):
            self.key = ...
            self.value = ...
            self.left = ...
            self.right = ...

    @staticmethod
    def create_node(key, value: Any, left: Optional[dict] = None, right: Optional[dict] = None) -> dict:
        """ Фабрика узлов """
        return {
            'key': key,
            'value': value,
            'left': left,
            'right': right
        }

    def __init__(self):
        self.root: Optional[dict] = None   # Корень дерева

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree

        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """
        if self.root is None:
            self.root = self.create_node(key, value)   # Если нет корня, то мы его создаем
        else:
            current_root = self.root
            while ...:   # ToDo
                root_key = current_root['key']
                if root_key == key:
                    raise KeyError('Дублируются ключи')
                current_root = current_root['right'] if key > root_key else current_root['left']
                if current_root is None:   # получаем лист(нет левого и правого)
                    ...   # ToDo Вставить элемент!

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:   # ToDo разбить на 3 метода (есть в лекции)
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        print(key)
        return None

    def find(self, key: int) -> Optional[Any]:   # ToDo
        """
        Find value by given key in the BST

        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        print(key)
        return None

    def clear(self) -> None:   # ToDo
        """
        Clear the tree

        :return: None
        """
        return None
