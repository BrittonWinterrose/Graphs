"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        
    def bft(self, starting_vertex):
        """ Breadth First Traversal
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty set to store visted nodes
        visited = set()

        vertex_pattern = []
        store_pattern = []
        check_count = 0

        # Create an empty Queue and enqueue the starting vertex
        q = Queue()
        q.enqueue(starting_vertex)
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            check_count += 1 
            # if that vertex has not been visted...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                vertex_pattern.append(v)
                # Then add all it's neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
                    store_pattern.append(neighbor)
        
        print(f"vertices traversed: {vertex_pattern}")
        print(f"traversal pattern: {store_pattern}")
        print(f"verticies checked: {check_count}")      

    def dft(self, starting_vertex):
        """ Depth First Traversal
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty set to store visited nodes
        visited = set()

        vertex_pattern = []
        store_pattern = []
        check_count = 0

        # Create an empty stack and push the starting vertex
        s = Stack()
        s.push(starting_vertex)
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            check_count += 1 
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                vertex_pattern.append(v)
                # Then add all of its neighbors to the top of the stack. 
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
                    store_pattern.append(neighbor)

        print(f"vertices traversed: {vertex_pattern}")
        print(f"traversal pattern: {store_pattern}")
        print(f"verticies checked: {check_count}")
        
    def dft_recursive(self, starting_vertex, visited = None):
        """ Depth First Traversal, Recursive
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Check if it is the first time visited is being initialized.
        if visited is None:
            visited = set()
        # If the vertex hasn't been visited...
        if starting_vertex not in visited:
            # Mark the node as visited.
            print(starting_vertex)
            visited.add(starting_vertex)
            # Then Call DFT_Recursive on each child.
            for child in self.vertices[starting_vertex]:
                self.dft_recursive(child, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """ Breadth First Search
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty set to store visited nodes
        visited = set()
        # Create an empty Queue and enqueue a path to the starting vertex
        q = Queue()
        # While the queue is not empty... 
        while q.size() > 0:
            # Dequeue the first path
            path = q.dequeue()
            # Grab the vertex from the end of the path
            v = path[-1]
            # If vertex == target, return path
            if v == destination_vertex:
                return path
            # IF that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Then add on a path for each of its neighbors to the back of the queue...
                for neighbor in self.vertices[v]:
                    # Copy the path 
                    path_copy = list(path)
                    # Append neighbor to the back of the copy
                    path_copy.append(neighbor)
                    # enqueue the copy back to the queue.
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """ Depth First Search
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty set to store visited nodes
        visited = set()
        # Create an empty stack and push a path to the starting vertex
        s = Stack()
        s.push([starting_vertex])
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first path
            path = s.pop()
            # Grab the vertex from the end of the path
            v = path[-1]
            # If vertex == target, return path
            if v == destination_vertex:
                return path        
            # If vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Then add on a path for each of its neighbors to the back of the queue...
                for neighbor in self.vertices[v]:
                    # Copy the path
                    path_copy = list(path)
                    # Append neighbor to back of the copy. 
                    path_copy.append(neighbor)
                    # add copy back onto the stack.
                    s.push(path_copy) 





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
