class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
 
        memo = {}
       
        def dfs(target):
            if target == 0:
                
                return 0
           
            if target in memo:
                return memo[target]
          
            res = 1e9
            for coin in coins:
                if (target-coin >= 0):
                    res = min(res, 1+dfs(target-coin))
            memo[target] = res
            return res
        minCoin = dfs(amount)
        return -1 if minCoin  >= 1e9 else minCoin