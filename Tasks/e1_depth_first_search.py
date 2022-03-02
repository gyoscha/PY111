from typing import Hashable, List
import networkx as nx


# def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
#     """
#     Do an depth-first search and returns list of nodes in the visited order
#
#     :param g: input graph
#     :param start_node: starting node of search
#     :return: list of nodes in the visited order
#     """
#     # вершина стэка справо
#     visited_nodes = {node: False for node in g.nodes}  # словарь из непосещенных узлов
#
#     wait_nodes = [start_node]  # стэк из узлов, которые ожидают обхода
#     visited_nodes[start_node] = True
#
#     path_nodes = []  # сюда должны помещаться узлы из стэка / "Сгоревшие узлы"
#
#     while wait_nodes:  # пока стэк существуют
#         current_node = wait_nodes.pop(-1)  # достаем горящий узел
#         path_nodes.append(current_node)
#
#         for neighbour in g[current_node]:
#             if not visited_nodes[neighbour]:
#                 wait_nodes.append(neighbour)  # подожгли соседа
#                 visited_nodes[neighbour] = True
#
#     return path_nodes


# Рекурсивный алгоритм поиска в глубину
def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    visited_nodes = {node: False for node in g.nodes}
    path_nodes = []

    def recursion_dfs(current_node):
        if visited_nodes[current_node]:   # базовый случай
            return None
        visited_nodes[current_node] = True
        path_nodes.append(current_node)

        for neighbour in g[current_node]:
            if not visited_nodes[neighbour]:
                recursion_dfs(neighbour)

        return path_nodes

    return recursion_dfs(start_node)
