class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}
        for i, n in enumerate(nums):
            if n not in hashMap:
                hashMap[target-n] = i
            else:
                return [hashMap[n], i]
        return []
