class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        def dfs(i):
            if i == len(nums):
                return 0
            
            LIS = 1
            for e in range(i+1, len(nums)):
                if nums[i] < nums[e]:
                    LIS = max(LIS, 1+dfs(e))
            return LIS


        return max([dfs(i) for i in range(len(nums))])