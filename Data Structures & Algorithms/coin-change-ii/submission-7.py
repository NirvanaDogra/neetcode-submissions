class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(target, i):
            
            if target == 0:
                return 1
            if target < 0:
                return 0
            if (i, target) in memo:
                return memo[(i, target)]
            
            total = 0
            for j in range(i, len(coins)):
                coin = coins[j]
                total+=dfs(target-coin, j)
            memo[(i, target)] = total
            return total
        return dfs(amount, 0)