class Solution:
    def numDecodings(self, s: str) -> int:
        dic = {}
        for i in range(1, 26+1):
            dic[i] = chr(ord("A")+i-1)
        
        res = []
        memo = {}
        def dfs(part, i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if i>len(s):
                return 0
            if int(s[i]) == int(0):
                return 0
            
            total = 0
            total+=dfs(s[i]+part, i+1)
            if (i+1) < len(s) and int(s[i]+s[i+1]) <=26 :
                t = dfs(s[i]+s[i+1]+part, i+2)
                total+=t
            memo[i] = total
            return total
        
        return dfs("", 0)


    
