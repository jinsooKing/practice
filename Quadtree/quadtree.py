import numpy as np

class Node:
    def __init__(self, data, leaf):
        self.data = data
        self.leaf = leaf
        self.child = [None, None, None, None]

class QuadTree:
    def __init__(self, grid):
        self.root = self.build_tree(grid, Node(0, False))
        
    def build_tree(self, grid, node):
        rows, cols = grid.shape

        if len(np.unique(grid)) == 1:
            node.leaf = True
            node.data = grid[0, 0]
        else:
            half_rows, half_cols = rows // 2, cols // 2
            quadrants = [
                grid[:half_rows, :half_cols],
                grid[:half_rows, half_cols:],
                grid[half_rows:, :half_cols],
                grid[half_rows:, half_cols:]
            ]
            
            for i, quadrant in enumerate(quadrants):
                node.child[i] = self.build_tree(quadrant, Node(0, False))
    
        return node

    def print_tree(self):
        code = self.preorder_traversal(self.root, '')
        print(code)
    
    def preorder_traversal(self, node, code):
        if node is not None:
            code += f'({node.data}, Leaf: {node.leaf}) ['
            for child in node.child:
                code = self.preorder_traversal(child, code)
            code += '] '
        return code

        