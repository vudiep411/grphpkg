from collections import defaultdict
from heapq import heappush, heappop

class WeightedGraph:
    def __init__(self, matrix=None):
        self.graph = defaultdict(list)
        self.adjacency_matrix = matrix

        if matrix is not None:
            self.__construct_graph_from_matrix()

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Make the graph undirected

    def __construct_graph_from_matrix(self):
        vertices = range(len(self.adjacency_matrix))
        self.graph = defaultdict(list)

        for i, u in enumerate(vertices):
            for j, v in enumerate(vertices):
                if u == v or self.adjacency_matrix[i][j] == float('inf'):
                    continue

                self.add_edge(u, v, self.adjacency_matrix[i][j])

    def print_graph(self):
        for k, neighbors in self.graph.items():
            print(f"{k} -> {neighbors}")

    def prim_mst(self, start):
        visited = set()
        min_heap = [(0, start, None)]
        mst_edges = []
        mst_cost = 0

        while min_heap:
            weight, current_vertex, parent = heappop(min_heap)
            if current_vertex not in visited:
                visited.add(current_vertex)
                if parent is not None:
                    mst_edges.append((parent, current_vertex, weight))
                    mst_cost += weight
                for neighbor, edge_weight in self.graph[current_vertex]:
                    if neighbor not in visited:
                        heappush(min_heap, (edge_weight, neighbor, current_vertex))
        return mst_edges, mst_cost