class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(subset, i):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            if sum(subset) > target or i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(subset, i)
            subset.pop()
            dfs(subset, i+1)
        
        dfs([], 0)
        return res
            