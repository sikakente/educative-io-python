def create_adjacency_list(num_nodes, edges):
    graph = [set() for _ in range(num_nodes)]
    for index, edge in enumerate(edges):
        v_1, v_2 = edge[0], edge[1]
        graph[v_1].add(v_2)
        graph[v_2].add(v_1)

    return graph
