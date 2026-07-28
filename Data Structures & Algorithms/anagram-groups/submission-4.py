class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        def getHash(word):
            nums = [0]*26
            for char in word:
                nums[ord(char)-ord('a')]+=1
            return tuple(nums)

        for word in strs:
            hashKey = getHash(word)
            if hashKey not in hashMap:
                hashMap[hashKey] = [word]
            else:
                hashMap[hashKey].append(word)
       
        return list(hashMap.values())