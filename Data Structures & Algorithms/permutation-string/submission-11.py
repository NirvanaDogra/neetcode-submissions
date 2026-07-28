class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        for i in s1:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
       
        left = 0
        right = left + len(dic.keys())
        lst = []
        while right<len(s2):
            if sorted(s2[left:right]) == sorted(s1):
                return True
            left+=1 
            right = left + len(s1)

        print((s2[left:right]), (s1))
        if sorted(s2[left:right]) == sorted(s1):
            return True
        return False