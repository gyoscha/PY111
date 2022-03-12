from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    visited = {node: False for node in g.nodes}
    total_costs = {node: float("inf") for node in g.nodes}
    current_node = starting_node
    total_costs[current_node] = 0

    while True:
        visited[current_node] = True
        print(total_costs)
        # обновляем стоимости всех соседей
        for neighbour_node in g[current_node]:
            edge = g[current_node][neighbour_node]
            weight = edge['weight']
            total_costs[neighbour_node] = min(
                total_costs[neighbour_node],
                total_costs[current_node] + weight)
        print(total_costs)

        # выбрать новый current_node
        not_visited_total_costs = {node: cost for node, cost in total_costs.items() if not visited[node]}
        if not not_visited_total_costs:
            break
        current_node, _ = min(
            not_visited_total_costs.items(),
            key=lambda item: item[1]
        )

    return total_costs


if __name__ == '__main__':
    G = nx.Graph()
    G.add_nodes_from("ABCDEFG")
    G.add_weighted_edges_from([
        ("A", "B", 1),
        ("B", "C", 3),
        ("C", "E", 4),
        ("E", "F", 3),
        ("B", "E", 8),
        ("C", "D", 1),
        ("D", "E", 2),
        ("B", "D", 2),
        ("G", "D", 1),
        ("D", "A", 2),
    ])

    print(dijkstra_algo(G, 'G'))
