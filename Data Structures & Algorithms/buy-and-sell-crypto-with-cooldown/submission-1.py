class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if buying:
                buy = dfs(i+1, False) - prices[i]
                dont = dfs(i+1, True)
                return max(buy, dont)
            else:
                sell = dfs(i+2, True) + prices[i]
                dont = dfs(i+1, False)
                return max(sell, dont)
        return dfs(0, True)
