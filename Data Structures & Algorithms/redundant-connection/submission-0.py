class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(1, len(edges)+1)}
        

        def dfs(curr, pre):
            # print(visit)
            if curr in visit:
                return True

            visit.add(curr)
            for child in adj[curr]:
                if child == pre:
                    continue
               
                if dfs(child, curr):
                    return True

            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            pre = -1
            visit = set()
            
            if dfs(u, -1):
                return [u, v]
        return []
