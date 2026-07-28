class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        map = {}
        for num in nums:
            if num-1 in nums:
                continue
            
            else:
                map[num] = []
                temp = num
                while temp+1 in nums:
                    map[num].append(temp+1)
                    temp+=1
                    print(map)
        
        maxVal = 0
        for key, value in map.items():
            maxVal = max(maxVal, len(value))
        return maxVal+1