class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = -9999
        ptr2 = 0
        minP = prices[ptr2]

        while ptr2 < len(prices):
            minP = min(minP, prices[ptr2])
            maxP = max(maxP, prices[ptr2]-minP)
            ptr2+=1

        return maxP
    #     if prices[ptr1] >  prices[ptr2]:
    #         ptr1+=1
    #         ptr2+=1
    #     else:
    #         maxP = max(maxP, prices[ptr2]-prices[ptr1])
    #         ptr2+=1
    # [0, -9, -5, -5, -3, -9]