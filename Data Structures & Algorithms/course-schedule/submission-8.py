class Solution:
    # dont complicate life by not adding keys. Do a for or adding all the value in dic ir. empty dependency
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {}

        for i, j in prerequisites:
            if i in dic:
                dic[i].append(j)
            else:
                dic[i] = [j]
        
        visited = set()

        def dfs(key):
            if key in visited:
                return False
            if key in dic:
                visited.add(key)
                dep = dic[key]
                print(key, dep)
                for d in dep:
                    if dfs(d) == False:
                        return False

            return True
        
        for i in dic.keys():
            if dfs(i) == False:
                return False
            visited = set()
        return True






