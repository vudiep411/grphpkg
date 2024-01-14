from __future__ import absolute_import
from collections import defaultdict

class Graph:
    def __init__(self, representation):
        self.graph = defaultdict(list)
        self.__construct_graph(representation)
    
    def __construct_graph(self, representation):
        if isinstance(representation, list):
            if isinstance(representation[0], list):
                # Adjacency Matrix
                self.__construct_graph_from_matrix(representation)
            else:
                # Adjacency List
                self.__construct_graph_from_list(representation)
        else:
            raise ValueError("Invalid representation type. Please provide a 2D list (matrix) or a list (adjacency list).")
        
    def __construct_graph_from_matrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    self.add_edge(i, j)

    def __construct_graph_from_list(self, adj_list):
        for u, neighbors in enumerate(adj_list):
            for v in neighbors:
                self.add_edge(u, v)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        for k, v in self.graph.items():
            print(f"{k} -> {v}")

    def bfs(self, start, callback):
        """Perform BFS and callback operation on each node

        * start: Starting node
        * callback: Your custom function to perform your operation 
        on each node
        """
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                callback(vertex)
                visited.add(vertex)
                queue.extend(neighbour for neighbour in self.graph[vertex] if neighbour not in visited)

    def dfs(self, start, callback):
        """Perform DFS and callback operation on each node
        
        * start: Starting node
        * callback: Your custom function to perform your operation 
        on each node
        """
        visited = set()
        def dfs_recursive(vertex):
            visited.add(vertex)
            callback(vertex)
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    dfs_recursive(neighbour)

        dfs_recursive(start)

    
