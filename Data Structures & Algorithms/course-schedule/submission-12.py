class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {}
        for i in range(numCourses):
            dic[i] = []
        
        for pre in prerequisites:
            x, y = pre
            dic[x].append(y)
        print(dic)

        visited = set()
        def dfs(course):
            print(course, course in visited)
            if course in visited:
                return False
            

            visited.add(course)
            for dep in dic[course]:
                if dfs(dep) == False:
                    return False
            visited.remove(course)
            return True

        for i in range(numCourses):
            visited= set()
            if not dfs(i):
                return False
        return True

                
