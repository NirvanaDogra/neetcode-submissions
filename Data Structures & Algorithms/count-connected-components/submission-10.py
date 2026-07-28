class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic  = {}
        for i in range(n):
            dic[i]= []
        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])
        

     
        visited = set()
        def dfs(node, pre):   
            visited.add(node)
            for i in dic[node]:
                if i not in visited:
                    dfs(i, node)

        
        count = 0
        for i in range(n):
            if i not in visited:
               count+=1
               print(dfs(i, -1))
               
          
        
        return count

        