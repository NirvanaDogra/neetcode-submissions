class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        dic = {}
        for i in nums:
            dic[i] = i
        
        maxV = max(nums)
        minV = min(nums)
        count = 0
        maxC =0
        for i in range(minV, maxV+1):
            if i in dic:
                print("found ", i)
                count +=1
            else:
                print("resetting mcoun till now",i, count)
                count=0
            maxC = max(maxC, count)
        return maxC
