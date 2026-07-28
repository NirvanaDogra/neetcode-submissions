class Solution:
    def isPalindrome(self, s: str) -> bool:
        # abc
        # abcd
        s = s.lower()
        newStr = ""
        for char in s:
            print(ord(char) not in range(ord('a'), ord('z')+1))
            if ord(char) not in range(ord('a'), ord('z')+1) and ord(char) not in range(ord('0'), ord('9')+1):
                continue
            else:
                newStr += char
                print(newStr)
        s = newStr
        print(newStr)


        ptr2 = len(s)//2
        ptr1 = ptr2

        if len(s) % 2 == 0:
            ptr1 = ptr2 -1
        

        while ptr1 >= 0 and ptr2 < len(s) and s[ptr1] == s[ptr2]:
            ptr1-=1
            ptr2+=1
        print(ptr1, ptr2)
        if ptr1!=-1 or ptr2!=len(s):
            return False
        
        return True
