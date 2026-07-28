class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        print(adj)

        pre = -1
        visit = set()

        def dfs(x, pre):
            print(x, pre)
            if x in visit:
                return

            visit.add(x)
            for i in adj[x]:
                if i == pre:
                    continue
                dfs(i, x)
            print(visit)
        
        count =0
        for i in range(n):
            print(visit)
            if i in visit:
                continue
            count+=1
            dfs(i, pre)
        return count 
            

        