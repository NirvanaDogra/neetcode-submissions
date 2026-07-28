class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        memo = {}
        def dfs(i):
            if i == len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            LIS = 1
            for e in range(i+1, len(nums)):
                if nums[i] < nums[e]:
                    LIS = max(LIS, 1+dfs(e))
            memo[i] = LIS
            return LIS


        return max([dfs(i) for i in range(len(nums))])