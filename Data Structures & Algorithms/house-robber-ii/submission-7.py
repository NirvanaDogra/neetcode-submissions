class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxRobber(ar):
            rob1, rob2 = 0, 0 
            for num in ar:
                newRob = max(num+rob1, rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2

        return max(nums[0], maxRobber(nums[0:len(nums)-1]), maxRobber(nums[1:]))