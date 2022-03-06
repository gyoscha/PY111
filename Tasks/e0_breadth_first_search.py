from typing import Hashable, List
from collections import deque   # Очередь

import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    # Конец справа, начало слева

    visited_nodes = {node: False for node in g.nodes}   # словарь из непосещенных узлов

    wait_nodes = deque()   # очередь из узлов, которые ожидают обхода
    wait_nodes.append(start_node)   # подожгли первый узел
    visited_nodes[start_node] = True

    path_nodes = []   # сюда должны помещаться узлы из очереди / "Сгоревшие узлы"

    while wait_nodes:   # пока очередь существуют
        current_node = wait_nodes.popleft()   # достаем горящий узел
        path_nodes.append(current_node)
        
        for neighbour in g[current_node]:
            if not visited_nodes[neighbour]:
                wait_nodes.append(neighbour)   # подожгли соседа
                visited_nodes[neighbour] = True

    return path_nodes


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('I', 'H'),
        ('H', 'D'),
        ('H', 'E'),
        ('H', 'J'),
        ('E', 'D'),
    ])

    print(graph['A'])

