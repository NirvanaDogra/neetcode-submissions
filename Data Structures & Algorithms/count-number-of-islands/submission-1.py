class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited =  set()

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0' or (i, j) in visited:
                return 

            visited.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j]=='1' and (i, j) not in visited:
                    dfs(i, j)
                    count+=1
                

        return count

