class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res =[]
        part = []
        
        def dfs(i):
            nonlocal part;
            if  i==len(s):
                res.append(part.copy())
                
                return
            for j in range(i, len(s)):
                sub = s[i:j+1]
                rev = sub[::-1]
                print(sub, rev)
                if sub == rev:
                    part.append(sub)
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res


                