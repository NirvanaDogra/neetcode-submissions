class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      if len(s) == 0:
        return 0
      if len(s) == 1:
        return 1
      x = 0
      dic= {}
      minLen = -1
      for i in range(0, len(s)):
        print(s[i], "in", dic, s[i] in dic)
        if s[i] in dic and dic[s[i]] >= x:
            minLen = max(minLen, i-x)
            x = dic[s[i]]+1
            dic[s[i]] = i
            print("x", x, minLen)

        else:
            dic[s[i]] = i
        print(dic)
      return max(minLen, len(s)-x)   

