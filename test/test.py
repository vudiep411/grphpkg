# main_script.py
import sys
import os

# Add the parent directory to the Python path
current_path = os.path.abspath(os.path.dirname(__file__))
project_path = os.path.abspath(os.path.join(current_path, '..'))
sys.path.append(project_path)

from graph.graph import Graph

matrix_representation = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

g = Graph(matrix_representation)
g.print_graph()
g.dfs(0, lambda x: print(x))