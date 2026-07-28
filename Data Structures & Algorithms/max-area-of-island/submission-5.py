class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(i, j):
            print(i, j)
            if (i not in range(0, len(grid)) or 
                j not in range(0, len(grid[0])) or 
                grid[i][j] == 0 or (i, j) in visited):
                return 0
            visited.add((i, j))
            return 1 + dfs(i+1, j) + dfs(i-1, j)+ dfs(i, j+1) + dfs(i, j-1)
        
        maxArea = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if (i, j) not in visited and grid[i][j] ==1:
                    area = dfs(i, j)
                    print(area)
                    maxArea = max(maxArea, area)
        return maxArea

            
