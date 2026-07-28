class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = 0
        def dfs(i, j):
            nonlocal count
            print(i, j)
            if i == m-1 and j == n-1:
                count+=1
            elif i == m-1:  
                dfs(i, j+1) 
            elif j==n-1: 
                dfs(i+1, j)
            else:
                dfs(i, j+1)
                dfs(i+1, j)

        dfs(0, 0)
        return count