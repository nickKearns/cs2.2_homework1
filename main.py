from graphs.graph import Graph
from graphs.weighted_graph import WeightedGraph, WeightedVertex
from util.file_reader import read_graph_from_file
# from graphs.weighted_graph import WeightedGraph


# Driver code
if __name__ == '__main__':

    # # Create the graph

    # graph = WeightedGraph()

    # # Add some vertices
    # graph.add_vertex('A')
    # graph.add_vertex('E')
    # graph.add_vertex('B')
    # graph.add_vertex('C')
    # graph.add_vertex('D')
    # graph.add_vertex('F')
    # graph.add_vertex('G')

    # # Add connections
    # graph.add_edge('A', 'B')
    # graph.add_edge('B', 'C')
    # graph.add_edge('B', 'D')
    # graph.add_edge('D', 'E')
    # graph.add_edge('F', 'G')

    # # Or, read a graph in from a file
    # # graph = read_graph_from_file('test_files/graph_small_directed.txt')

    # # Output the vertices & edges
    # # Print vertices
    # print(f'The vertices are: {graph.get_vertices()} \n')

    # # Print edges
    # print('The edges are:')
    # for vertex_obj in graph.get_vertices():
    #     for neighbor_obj in vertex_obj.get_neighbors():
    #         print(f'({vertex_obj.get_id()} , {neighbor_obj.get_id()})')

    # # Search the graph
    # print('Performing BFS traversal...')
    # graph.bfs_traversal('A')

    # # Find shortest path
    # print('Finding shortest path from vertex A to vertex E...')
    # shortest_path = graph.find_shortest_path('A', 'E')
    # print(shortest_path)

    # # Find all vertices N distance away
    # print('Finding all vertices distance 2 away...')
    # vertices_2_away = graph.find_vertices_n_away('A', 2)
    # print(vertices_2_away)
    vertex_a = WeightedVertex('a')
    vertex_b = WeightedVertex('b')
    vertex_c = WeightedVertex('c')
    vertex_d = WeightedVertex('d')
    vertex_e = WeightedVertex('e')
    vertex_f = WeightedVertex('f')

    graph = WeightedGraph(False)

    graph.add_vertex(vertex_a.get_id())
    graph.add_vertex(vertex_b.get_id())
    graph.add_vertex(vertex_c.get_id())
    graph.add_vertex(vertex_d.get_id())
    graph.add_vertex(vertex_e.get_id())
    graph.add_vertex(vertex_f.get_id())



    graph.add_edge(vertex_a.get_id(), vertex_b.id, 5)
    graph.add_edge(vertex_b.get_id(), vertex_c.id, 1)
    graph.add_edge(vertex_c.get_id(), vertex_d.id, 2)
    graph.add_edge(vertex_d.get_id(), vertex_a.id, 4)
    graph.add_edge(vertex_e.get_id(), vertex_a.id, 10)
    graph.add_edge(vertex_f.get_id(), vertex_e.id, 5)
    graph.add_edge(vertex_f.get_id(), vertex_a.id, 3)

    # print(graph.minimum_spanning_tree_kruskal())
    # print(graph.minimum_spanning_tree_prim())
    # print(graph.floyd_warshall())
    print(graph.find_shortest_path('a', 'd'))