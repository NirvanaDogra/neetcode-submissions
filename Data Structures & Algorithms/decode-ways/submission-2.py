class Solution:
    def numDecodings(self, s: str) -> int:
        dic = {}
        for i in range(1, 26+1):
            dic[i] = chr(ord("A")+i-1)
        
        res = []
        def dfs(part, i):
            if i == len(s):
                res.append(part)
                return
            if i>len(s):
                return
            if int(s[i]) == int(0):
                return
            dfs(s[i]+part, i+1)
            if (i+1) < len(s) and int(s[i]+s[i+1]) <=26 :
                dfs(s[i]+s[i+1]+part, i+2)
        dfs("", 0)
        return len(res)


    
