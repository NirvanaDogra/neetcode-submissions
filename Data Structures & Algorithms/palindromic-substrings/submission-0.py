class Solution:
    def countSubstrings(self, s: str) -> str:
        res =[]

        for i in range(len(s)):
            print(i)
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print(s[l:r+1])
                res.append(s[l:r+1])
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res.append(s[l:r+1])
                l -= 1
                r += 1

            print(res)
        return len(res)