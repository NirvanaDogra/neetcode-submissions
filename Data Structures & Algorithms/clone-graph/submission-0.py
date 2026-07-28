"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Dictionary to store cloned nodes
        visited = {}

        def dfs(node):
            if node in visited:
                # Return the cloned node if it already exists
                return visited[node]

            # Clone the node
            clone = Node(node.val, [])
            visited[node] = clone  # Mark it as visited

            # Clone all neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)