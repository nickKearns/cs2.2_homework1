from collections import deque

class Vertex(object):
    """
    Defines a single vertex and its neighbors.
    """

    def __init__(self, vertex_id):
        """
        Initialize a vertex and its neighbors dictionary.
        
        Parameters:
        vertex_id (string): A unique identifier to identify this vertex.
        """
        self.__id = vertex_id
        self.__neighbors_dict = {} # id -> object

    def add_neighbor(self, vertex_obj):
        """
        Add a neighbor by storing it in the neighbors dictionary.

        Parameters:
        vertex_obj (Vertex): An instance of Vertex to be stored as a neighbor.
        """
        self.__neighbors_dict[vertex_obj.__id] = vertex_obj

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        neighbor_ids = list(self.__neighbors_dict.keys())
        return f'{self.__id} adjacent to {neighbor_ids}'

    def __repr__(self):
        """Output the list of neighbors of this vertex."""
        return self.__str__()

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return list(self.__neighbors_dict.values())

    def get_id(self):
        """Return the id of this vertex."""
        return self.__id


class Graph:
    """ Graph Class
    Represents a directed or undirected graph.
    """
    def __init__(self, is_directed=True):
        """
        Initialize a graph object with an empty vertex dictionary.

        Parameters:
        is_directed (boolean): Whether the graph is directed (edges go in only one direction).
        """
        self.__vertex_dict = {} # id -> object
        self.__is_directed = is_directed

    def add_vertex(self, vertex_id):
        """
        Add a new vertex object to the graph with the given key and return the vertex.
        
        Parameters:
        vertex_id (string): The unique identifier for the new vertex.

        Returns:
        Vertex: The new vertex object.
        """
        new_vertex = Vertex(vertex_id)
        self.__vertex_dict[vertex_id] = new_vertex
        return new_vertex
        

    def get_vertex(self, vertex_id):
        """Return the vertex if it exists."""
        if vertex_id not in self.__vertex_dict:
            return None

        vertex_obj = self.__vertex_dict[vertex_id]
        return vertex_obj

    def add_edge(self, vertex_id1, vertex_id2):
        """
        Add an edge from vertex with id `vertex_id1` to vertex with id `vertex_id2`.

        Parameters:
        vertex_id1 (string): The unique identifier of the first vertex.
        vertex_id2 (string): The unique identifier of the second vertex.
        """
        vertex1 = self.get_vertex(vertex_id1)
        vertex2 = self.get_vertex(vertex_id2)
        vertex1.add_neighbor(vertex2)
        if self.__is_directed == False:
            vertex2.add_neighbor(vertex1)
        
        
    def get_vertices(self):
        """
        Return all vertices in the graph.
        
        Returns:
        List<Vertex>: The vertex objects contained in the graph.
        """
        return list(self.__vertex_dict.values())

    def contains_id(self, vertex_id):
        return vertex_id in self.__vertex_dict

    def __str__(self):
        """Return a string representation of the graph."""
        return f'Graph with vertices: {self.get_vertices()}'

    def __repr__(self):
        """Return a string representation of the graph."""
        return self.__str__()

    def bfs_traversal(self, start_id):
        """
        Traverse the graph using breadth-first search.
        """
        if not self.contains_id(start_id):
            raise KeyError("One or both vertices are not in the graph!")

        # Keep a set to denote which vertices we've seen before
        seen = set()
        seen.add(start_id)

        # Keep a queue so that we visit vertices in the appropriate order
        queue = deque()
        queue.append(self.get_vertex(start_id))

        while queue:
            current_vertex_obj = queue.popleft()
            current_vertex_id = current_vertex_obj.get_id()

            # Process current node
            print('Processing vertex {}'.format(current_vertex_id))

            # Add its neighbors to the queue
            for neighbor in current_vertex_obj.get_neighbors():
                if neighbor.get_id() not in seen:
                    seen.add(neighbor.get_id())
                    queue.append(neighbor)

        return # everything has been processed

    def find_shortest_path(self, start_id, target_id):
        """
        Find and return the shortest path from start_id to target_id.

        Parameters:
        start_id (string): The id of the start vertex.
        target_id (string): The id of the target (end) vertex.

        Returns:
        list<string>: A list of all vertex ids in the shortest path, from start to end.
        """
        if not self.contains_id(start_id) or not self.contains_id(target_id):
            raise KeyError("One or both vertices are not in the graph!")

        # vertex keys we've seen before and their paths from the start vertex
        vertex_id_to_path = {
            start_id: [start_id] # only one thing in the path
        }

        # queue of vertices to visit next
        queue = deque() 
        queue.append(self.get_vertex(start_id))

        # while queue is not empty
        while queue:
            current_vertex_obj = queue.popleft() # vertex obj to visit next
            current_vertex_id = current_vertex_obj.get_id()

            # found target, can stop the loop early
            if current_vertex_id == target_id:
                break

            neighbors = current_vertex_obj.get_neighbors()
            for neighbor in neighbors:
                if neighbor.get_id() not in vertex_id_to_path:
                    current_path = vertex_id_to_path[current_vertex_id]
                    # extend the path by 1 vertex
                    next_path = current_path + [neighbor.get_id()]
                    vertex_id_to_path[neighbor.get_id()] = next_path
                    queue.append(neighbor)
                    # print(vertex_id_to_path)

        if target_id not in vertex_id_to_path: # path not found
            return None

        return vertex_id_to_path[target_id]




    def find_vertices_n_away(self, start_id, target_distance):
        """
        Find and return all vertices n distance away.
        
        Arguments:
        start_id (string): The id of the start vertex.
        target_distance (integer): The distance from the start vertex we are looking for

        Returns:
        list<string>: All vertex ids that are `target_distance` away from the start vertex
        """



        
        vertices_queue = deque()  #vertices_queue holds the vertex object itself
        distances_dict = {}  #distances dict holds the IDs of the vertices

        target_vertices = []


        vertices_queue.append(self.get_vertex(start_id))  
        distances_dict[start_id] = 0


        while vertices_queue:
            current_vertex_obj = vertices_queue.popleft()
            current_vertex_id = current_vertex_obj.get_id()


            
            
            if distances_dict[current_vertex_id] == target_distance:
                target_vertices.append(current_vertex_id)


            for neighbor in current_vertex_obj.get_neighbors():
                neighbor_id = neighbor.get_id()
                if neighbor_id not in distances_dict:
                    neighbor_distance = distances_dict[current_vertex_id] + 1
                    distances_dict[neighbor_id] = neighbor_distance
                    vertices_queue.append(neighbor)



        
        return target_vertices





    def is_bipartite(self):
        """
        Return True if the graph is bipartite, and False otherwise.
        """

        #initialize a queue that will be used for BFS traversal
        queue = deque()

        # initiate a dictionary where the keys are 1 and -1  and the values are the list the vertices belong to

        vertex_group = {1: [], -1: []}

        #this value will be multiplied by -1 on each iteration and then used to add vertices to either the 
        #list associated with 1 or the list associated with -1
        key_tracker = 1



        #get the first vertex in the vertex dict as starting point for BFS
        start_vertex = self.get_vertices()[0]


        #add the vertex to the vertex group dictionary using the key tracker and add the id of the vertex NOT THE OBJECT to the list
        vertex_group[key_tracker].append(start_vertex.get_id())

        #begin BFS by appending the starting vertex 
        queue.append(start_vertex) 

        seen_vertices = set()

        while queue:
            current_vertex_obj = queue.popleft()
            current_vertex_id = current_vertex_obj.get_id()
            # seen_vertices.add(current_vertex_id)
            #find which group current_vertex belongs to 
            if current_vertex_id in vertex_group[1]:
                key_tracker = 1
            elif current_vertex_id in vertex_group[-1]:
                key_tracker = -1

            seen_vertices.add(current_vertex_id)
            print('Processing vertex {}'.format(current_vertex_id))
            for neighbor in current_vertex_obj.get_neighbors():


                neighbor_id = neighbor.get_id()

                #flipping the key_tracker so the neighbors can be added to the other group
                temp_key_tracker = key_tracker * -1
                vertex_group[temp_key_tracker].append(neighbor_id)
                if neighbor_id in vertex_group[key_tracker]:
                    return False

                elif neighbor.get_id() not in seen_vertices:
                    queue.append(neighbor)
        return True










        




    def find_connected_components(self):
        """
        Return a list of all connected components, with each connected component
        represented as a list of vertex ids.
        """

        connected_comp_list = []

        visited = set()



        def dfs_traversal_recursive(vertex, visited_vertices, connected_vertices):
            print(f'Visiting vertex {vertex.get_id()}')

            visited_vertices.add(vertex)
            connected_vertices.append(vertex.get_id())

            # recurse for each vertex in neighbors
            for neighbor in vertex.get_neighbors():
                if neighbor not in visited_vertices:
                    dfs_traversal_recursive(neighbor, visited_vertices, connected_vertices)
            return connected_vertices


        for vertex in self.get_vertices():
            if vertex not in visited:
                # visited.add(vertex)
                current_connected_vertices = []
                dfs_traversal_recursive(vertex, visited, current_connected_vertices)
                connected_comp_list.append(current_connected_vertices)


        return connected_comp_list
             



    def find_path_dfs_iter(self, start_id, target_id):
        """
        Use DFS with a stack to find a path from start_id to target_id.
        """

        stack = deque()
        starting_vertex = self.get_vertex(start_id)
        stack.append(starting_vertex)


        path = []

        seen_vertices = set()


        while stack:
            current_vertex_obj = stack.pop()
            current_vertex_id = current_vertex_obj.get_id()

            #if the function has reached its target vertex
            if current_vertex_id == target_id:
                path.append(current_vertex_id)
                return path

            path.append(current_vertex_id)

            for neighbor in current_vertex_obj.get_neighbors():
                if neighbor not in seen_vertices:
                    stack.append(neighbor)
                    seen_vertices.add(neighbor.get_id())
                
                



        

    def dfs_traversal(self, start_id):
        """Visit each vertex, starting with start_id, in DFS order."""

        visited = set() # set of vertices we've visited so far

        def dfs_traversal_recursive(start_vertex):
            print(f'Visiting vertex {start_vertex.get_id()}')

            # recurse for each vertex in neighbors
            for neighbor in start_vertex.get_neighbors():
                if neighbor.get_id() not in visited:
                    visited.add(neighbor.get_id())
                    dfs_traversal_recursive(neighbor)
            return

        visited.add(start_id)
        start_vertex = self.get_vertex(start_id)
        dfs_traversal_recursive(start_vertex)

    def contains_cycle(self):
        """
        Return True if the directed graph contains a cycle, False otherwise.
        """

        visited_vertices = set()


        for vertex in self.get_vertices():
            if vertex not in visited_vertices:
                path_list = []
                contains_cycle = self.contains_cycle_recursive(vertex, visited_vertices, path_list)
        return contains_cycle
        
    def contains_cycle_recursive(self, vertex, visited_vertices, path_list):
        contains_cycle = False

        visited_vertices.add(vertex)
        path_list.append(vertex)

        for neighbor in vertex.get_neighbors():
            if neighbor not in path_list:
                contains_cycle = self.contains_cycle_recursive(neighbor, visited_vertices, path_list)
            elif neighbor in path_list:
                return True
        path_list.remove(vertex)

        return contains_cycle


            
            

            

            
        





    def topological_sort(self):
        """
        Return a valid ordering of vertices in a directed acyclic graph.
        If the graph contains a cycle, throw a ValueError.
        """
        # TODO: Create a stack to hold the vertex ordering.

        solution_stack = deque()


        if self.contains_cycle():
            raise ValueError("graph contains cycle cannot be sorted")

        visited = set()


        # TODO: For each unvisited vertex, execute a DFS from that vertex.
        def recursive_topo(vertex, visited_vertices, stack):

            visited_vertices.add(vertex)

            for neighbor in vertex.get_neighbors():
                if neighbor not in visited_vertices:
                    recursive_topo(neighbor, visited_vertices, stack)
            # TODO: On the way back up the recursion tree (that is, after visiting a 
            # vertex's neighbors), add the vertex to the stack.
            stack.append(vertex.get_id())
            return stack
       

        for vertex in self.get_vertices():
            if vertex not in visited:
                recursive_topo(vertex, visited, solution_stack)
        
        solution_list = []

        for vertex_id in range(len(solution_stack)):
            solution_list.append(solution_stack.pop())

        return solution_list
            

        # TODO: Reverse the contents of the stack and return it as a valid ordering.

        # answer = []
        # for entry in s:
        #     answer.append(s.pop())
        # return answer
            









