class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dic = {}
        for i in range(n):
            dic[i] = []
        
        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])
        
        visited = set()
        cycle = set()
        def hasCycle(i, prev):
            if i in cycle:
                return True
            visited.add(i)
            cycle.add(i)
            for dep in dic[i]:
                if dep != prev:
                    if hasCycle(dep, i):
                        return True
            cycle.remove(i)
            return False
        
        info =  hasCycle(0, -1)
        print(visited)
        if info:
            return False
        return len(visited) == n
                

        
