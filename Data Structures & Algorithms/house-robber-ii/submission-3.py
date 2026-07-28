class Solution:
    def rob(self, nums: List[int]) -> int:
        def getRobbMax(nums):
            nums.append(0)
            for i in range(len(nums)-3, -1, -1):
                nums[i] = max(nums[i+1], nums[i]+nums[i+2])
            print(nums)
            return nums[0]
        
        if len(nums) == 1:
            return nums[0]

        return max(getRobbMax(nums[0:len(nums)-1]), 
                    getRobbMax(nums[1:len(nums)]))