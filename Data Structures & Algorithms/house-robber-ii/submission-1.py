class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def getMax(nums):
            rob1 = 0
            rob2 = 0 
            for i, n in enumerate(nums):
                temp = max(rob1+n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(getMax(nums[1:]), getMax(nums[:-1]))
       