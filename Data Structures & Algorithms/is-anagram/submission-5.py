class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ar = [0 * i for i in range(26)]

        for i in s:
            ar[ord(i)-ord('a')] += 1
        
        for i in t:
             ar[ord(i)-ord('a')] -= 1
        print(ar)
        for i in ar:
            if i!=0:
                return False
        return True

        

