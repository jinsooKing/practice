import numpy as np
from collections import deque
from problem import *
import heapq


def build_graph(maze, start, destination):
    """ Build a graph in adjacency list representation

        You should assign the vertex index for each path (i, j) in the ascending order
        of the number 100 * i + j. For example, if there exists only two paths in the 
        maze with coordinates (10, 10) and (10, 11). The path (10, 10) has the index 0. 
        The other one has the index 1.

    Args:
        maze (list): maze values represents whether there is a path (1) or not (0)
        start (list): a start coordinate
        destination (list): a destination coordinate

    Returns:
        graph (list): an adjacency list representation of maze graph
        start (int): a start vertex index
        destination (int): a destinatnon vertex index

    """
    rows, cols = len(maze), len(maze[0])
    graph = {}
    vertex_index = {}
    index_counter = 0

    def get_index(i, j):
        return 100 * i + j

    def add_edge(u, v):
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
        
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                current_index = get_index(i, j)
                vertex_index[(i, j)] = current_index
                
                neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                for neighbor in neighbors:
                    ni, nj = neighbor
                    if 0 <= ni < rows and 0 <= nj < cols and maze[ni][nj] == 1:
                        neighbor_index = get_index(ni, nj)
                        add_edge(current_index, neighbor_index)

    start = vertex_index[tuple(start)]
    destination = vertex_index[tuple(destination)]

    return graph, start, destination


def dfs(graph, start, destination):
    """ Find destination node using a depth first search (DFS) algorithm
        
        DFS should halt when it visits the destination vertex. 
        DFS should determine the next visit vertex in ascending order of vertex indices. 
        For example, if dfs currently visits the vertex 6 whose neighbors are 9, 3, 20, 
        then the next visited vertex will be 3.

    Args:
        graph (list): an adjacency list representation of maze graph
        start (int): a start vertex index
        destination (int): a destinatnon vertex index

    Returns:
        success (bool): True if visits the destination vertex. False otherwise
        history (list): the vertex indices in visiting order
    """
    stack = [start]
    visited = set()
    history = []

    while stack:
        current_vertex = stack.pop()
        history.append(current_vertex)

        if current_vertex == destination:
            return True, history

        if current_vertex not in visited:
            visited.add(current_vertex)
            neighbors = sorted(graph.get(current_vertex, []))
            stack.extend(neighbors)

    return False, history


def bfs(graph, start, destination):
    """ Find destination node using a breadth first search (BFS) algorithm.
        
    Args:
        graph (list): an adjacency list representation of maze graph
        start (int): a start vertex index
        destination (int): a destinatnon vertex index

    Returns:
        success (bool): True if visits the destination vertex. False otherwise
        history (list): the vertex indices in visiting order
    """
    visited = set() 
    queue = deque([start]) 
    history = [] 

    while queue:
        current_vertex = queue.popleft()
        history.append(current_vertex)

        if current_vertex == destination:
            return True, history 

        visited.add(current_vertex)

        for neighbor in graph.get(current_vertex, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return False, history


def astar(graph, start, destination):
    """ Find destination node using a A* algorithm.

    Args:
        graph (list): an adjacency list representation of maze graph
        start (int): a start vertex index
        destination (int): a destinatnon vertex index

    Returns:
        success (bool): True if visits the destination vertex. False otherwise
        history (list): the vertex indices in visiting order
    """
    def heuristic(node, destination): # 맨해튼 거리 함수
        return abs(node // 100 - destination // 100) + abs(node % 100 - destination % 100) 

    priority_queue = [(heuristic(start, destination), 0, start)]
    heapq.heapify(priority_queue)

    visited = {start: 0}
    
    history = []

    while priority_queue:
        _, cost, current_node = heapq.heappop(priority_queue)
        
        if current_node == destination:
            return True, history + [current_node]

        for neighbor in graph.get(current_node, []):
            new_cost = cost + 1  
            if neighbor not in visited or new_cost < visited[neighbor]:
                visited[neighbor] = new_cost
                heapq.heappush(priority_queue, (new_cost + heuristic(neighbor, destination), new_cost, neighbor))

        history.append(current_node)

    return False, history