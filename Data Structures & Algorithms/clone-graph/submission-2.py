"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if  node == None:
            return None
        visited = {}
        def deepCopy(node):
            
            if node in visited:
                return visited[node]
            
            copy = Node(node.val, [])
            visited[node] = copy
            
            for nbr in node.neighbors:
               
                nbrCopy = deepCopy(nbr)
                copy.neighbors.append(nbrCopy)
            return copy
        
        return deepCopy(node)