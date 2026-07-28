class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = [0] * k
        dic = {}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
        
        arVal = list(dic.values())[:]
        arKey = list(dic.keys())[:]
        print(arVal, arKey)
        for i in range(len(arVal)):
            for j in range(0, len(arVal)-1):
                if arVal[j] < arVal[j+1]:
                    temp = arVal[j]
                    arVal[j] = arVal[j+1]
                    arVal[j+1] = temp

                    temp = arKey[j]
                    arKey[j] = arKey[j+1]
                    arKey[j+1] = temp
        return arKey[:k]
            
