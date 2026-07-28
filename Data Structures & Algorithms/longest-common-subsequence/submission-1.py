class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ar = []
        for i in range(0, len(text1)+1):
            temp  = [0 for j in range(0, len(text2)+1)]
            ar.append(temp)
        
        
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text2[j] == text1[i]:
                    ar[i][j] = 1 + ar[i+1][j+1]
                else:
                    ar[i][j] = max(ar[i][j+1], ar[i+1][j])
        return ar[0][0]
