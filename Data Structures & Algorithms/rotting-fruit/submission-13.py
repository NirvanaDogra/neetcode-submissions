class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    fresh+=1
                
        
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dx, dy in direction:
                    row = r+dx
                    col = c+dy
                    
                    if ((row, col) not in visited and row in range (0, rows) and 
                        col in range(0, cols) and grid[row][col] == 1):
                        q.append((row, col))
                        
                        fresh +=-1
                    visited.add((row, col))
                
            time+=1
        if fresh > 0:
            return -1
        if time == 0:
            return 0
        return   time -1