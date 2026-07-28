class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(i, j):
            nonlocal count;
            if (i, j) in visited:
                return 0
            if i<0 or i>= rows:
                return 0
            if j<0 or j >= cols:
                return 0
            
            if grid[i][j] == "1":
                visited.add((i, j))
                down = dfs(i+1, j)
                up = dfs(i-1, j)
                right = dfs(i, j+1)
                left = dfs(i, j-1)

          
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count+=1
                
        return count
            