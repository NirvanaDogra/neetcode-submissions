class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            for wrd in wordDict:
                l = len(wrd)
                underConsider = s[i: i+l]
                if wrd == underConsider:
                    if dfs(i+l):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)
