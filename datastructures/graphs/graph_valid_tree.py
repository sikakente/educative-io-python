"""
Problem Statement
----------------
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.  Return true if the edges of the given graph make up a valid tree, and false otherwise.


Input
-----
list of edges and number of vertices

Output
-------
true of false
"""
from collections import defaultdict
from datastructures.graphs.utils import create_adjacency_list


def valid_tree(n, edges):
    graph = create_adjacency_list(n, edges)
    if not graph and n > 1:
        return False
    if not graph and n <= 1:
        return True
    is_visited = [-1] * n
    queue = [0]
    is_visited[0] = 0
    has_cycle = False

    while queue and not has_cycle:
        current_vertex = queue.pop(0)
        is_visited[current_vertex] += 1

        adjacent_vertices = graph[current_vertex]
        for adj_vertex in adjacent_vertices:
            if is_visited[adj_vertex] == 0:
                has_cycle = True
                break
            if is_visited[adj_vertex] == -1:
                is_visited[adj_vertex] += 1
                queue.append(adj_vertex)

    not_all_nodes_visited = -1 in is_visited
    return False if has_cycle or not_all_nodes_visited else True


if __name__ == '__main__':
    import doctest

    doctest.testmod()
