class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        for char in s:
            if char not in hashMap:
                hashMap[char] = 1
            else:
                hashMap[char] += 1
        
        for char in t:
            if char in hashMap:
                hashMap[char] -= 1
            else:
                return False
        
        for key, val in hashMap.items():
            if val > 0:
                return False
        
        return True


