class Solution:
    # unidirection graph [[0,1],[2,0],[3,0],[1,4]] so 0 -> 1 but 0-> 2 if we dont add the edges
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dic  = {}
        for i in range(n):
            dic[i]= []
        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])
        

        hasVisited = set()
        visited = set()
        def dfs(node, pre):
            if node in hasVisited:
                return False
            print(node)
            hasVisited.add(node)
            visited.add(node)
            for i in dic[node]:
                if i!= pre:
                    if not dfs(i, node):
                        return False
            hasVisited.remove(node)
                    
            return True
        
        res = dfs(i, -1)
        if not res:
            return False
            
        if len(visited) == n:
            return True 
        else:
            return False


