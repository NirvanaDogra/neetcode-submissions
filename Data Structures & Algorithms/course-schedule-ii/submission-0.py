class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        path =[]
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitSet = []

        def dfs(crs):
            if crs in visitSet:
                return False
            if len(preMap[crs]) == 0:
                if crs not in path:
                    path.append(crs)
                return True
            
            visitSet.append(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            path.append(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return []
        print(path)
        return path
    
        