"""
Problem Statement
----------------
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.  Return the number of connected components in the graph.


Input
-----
a number of edges

Output
-------
number of connected components
"""
from datastructures.graphs.utils import create_adjacency_list


def num_connected_components(n, edges):
    graph = create_adjacency_list(n, edges)
    is_visited = [False for _ in range(n)]

    def get_neighbours(vertex):
        return graph[vertex]

    def dfs(vertex):
        if is_visited[vertex]:
            return
        is_visited[vertex] = True
        for neighbour in get_neighbours(vertex):
            if not is_visited[neighbour]:
                dfs(neighbour)

    connection_count = 0
    for node in range(n):
        if not is_visited[node]:
            dfs(node)
            connection_count += 1

    return connection_count


if __name__ == '__main__':
    import doctest

    doctest.testmod()
