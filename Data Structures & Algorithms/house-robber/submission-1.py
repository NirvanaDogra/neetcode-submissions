class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        for i in range(len(nums)-3, -1, -1):
            nums[i] = max(nums[i+1], nums[i]+nums[i+2])
        print(nums)
        return nums[0]