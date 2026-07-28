class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] = dic[i]+1
            else:
                dic[i] = 1
               
        print(dic)
        for key in dic:
            if dic[key] > 1:
                return key