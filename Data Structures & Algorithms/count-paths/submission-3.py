class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       
        memo = {}
        def dfs(i, j):
            # print(i, j)
            count =0
            if (i, j) in memo:
                return memo[(i, j)]
            if i == m-1 and j == n-1:
                return 1;
            elif i == m-1:  
                count+=dfs(i, j+1) 
            elif j==n-1: 
                count+=dfs(i+1, j)
            else:
                count+=dfs(i, j+1)
                count+=dfs(i+1, j)
            
            memo[(i, j)] = count
            return count

       
        return  dfs(0, 0)