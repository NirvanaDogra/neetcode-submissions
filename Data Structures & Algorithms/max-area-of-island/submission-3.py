class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j, count):
            print(i, j, count)
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            count = 1+ dfs(i+1, j, count) + dfs(i-1, j, count) + dfs(i, j+1, count) + dfs(i, j-1, count)
            return count
        
        area = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = dfs(i, j, 0)
                    print(res)
                    area.append(res)
        if len(area) == 0:
            return 0
        return max(area)

            
