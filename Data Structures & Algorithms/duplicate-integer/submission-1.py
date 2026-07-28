class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if i in dic:
                return True
            dic[i] = 0
        return False