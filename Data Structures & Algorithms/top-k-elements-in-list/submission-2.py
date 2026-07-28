class Solution:
    def topKFrequent(self, nums:List[int], k: int) -> List[int]:
        ar = [ []  for i in range(len(nums)+1) ]
        feqMap = {}
        # freq
        for num in nums:
            print(num)
            if num in feqMap:
                feqMap[num] += 1
            else:
                feqMap[num] = 1
        print(feqMap)

        for key, value in feqMap.items():
            ar[value].append(key)
		
        print(ar)
        result = []
        for i in range(len(ar)-1, -1, -1):
            for j in range(len(ar[i])-1, -1, -1):
                result.append(ar[i][j])
                if len(result) == k:
                    return result
        return result

