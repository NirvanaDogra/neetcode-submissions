class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
    
        def dfs(l, r, temp):
            
            if l == n and l == r:
                result.append(temp)
            else:
                if l == r and l !=n:
                    dfs(l+1, r, temp+'(')
                if l == n and l > r:
                    dfs(l, r+1, temp+')')
                if l > r and l < n:
                    dfs(l+1, r, temp+'(')
                    dfs(l, r+1, temp+')')
            

        dfs(1, 0, "(")
        return result
            
