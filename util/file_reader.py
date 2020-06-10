from graphs.graph import Graph


def read_graph_from_file(filename):
    """
    Read in data from the specified filename, and create and return a graph
    object corresponding to that data.

    Arguments:
    filename (string): The relative path of the file to be processed

    Returns:
    Graph: A directed or undirected Graph object containing the specified
    vertices and edges
    """

    # TODO: Use 'open' to open the file

    with open(filename) as f:
        text_lines = f.readlines()


    

    # TODO: Use the first line (G or D) to determine whether graph is directed 
    # and create a graph object



    if text_lines[0].strip() == 'G':
        is_digraph = False
    elif text_lines[0].strip() == 'D':
        is_digraph = True
    else:
        raise ValueError("improper graph type")

    graph = Graph(is_digraph)

    # TODO: Use the second line to add the vertices to the graph

    for vertex_id in text_lines[1].strip('\n').split(','):
        graph.add_vertex(vertex_id)
    


    # TODO: Use the 3rd+ line to add the edges to the graph

    for edges in text_lines[2:]:
        new_edge = edges.strip('() \n').split(',')
        graph.add_edge(new_edge[0], new_edge[1])


    return graph

if __name__ == '__main__':

    graph = read_graph_from_file('test.txt')

    print(graph)