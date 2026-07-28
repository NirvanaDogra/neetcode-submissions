class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = {}
        output = []
        for i in range(numCourses):
            dic[i] = []
        
        for pre in prerequisites:
            x, y = pre
            dic[x].append(y)
        print(dic)

        cycle = set()
        visited = set()
        def dfs(i):
            if i in visited:
                return True
            if i in cycle:
                return False

            cycle.add(i)
            for dep in dic[i]:
                if dfs(dep) == False:
                    return False
            visited.add(i)
            cycle.remove(i)
            output.append(i)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
            print(visited)
            
        print(visited)
        return output