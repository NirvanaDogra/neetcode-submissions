class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newS = ""
        for i in s:
            if (i >= 'a' and i <='z') or (i>='0' and i<='9'):
                newS+=i
        print(newS, newS[::-1] )
        return newS == newS[::-1]
