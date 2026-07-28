from collections import Counter;
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        for i in range(len(nums)+1):
            frequencyMap[i] = []
    

        countedItemsMap = Counter(nums)

        for key, value in countedItemsMap.items():
            frequencyMap[value].append(key)
        # print(frequencyMap)
        topKValues = []
        for i in range(len(nums), -1, -1):
            if len(frequencyMap[i])!=0:
                topKValues.extend(frequencyMap[i][:])
            if len(topKValues) >= k:
                break
        return topKValues[0:k]


