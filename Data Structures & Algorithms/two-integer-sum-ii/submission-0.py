class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        dic = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if nums[i] in dic:
                return [dic[nums[i]]+1, i+1]
            dic[n] = i
            # print(dic)
        return []