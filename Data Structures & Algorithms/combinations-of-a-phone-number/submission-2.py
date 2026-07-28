class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if digits == "":
            return []

        res = []
        def dfs(i, s):
            
            if i == len(digits):
                res.append(s[:])
                return


            for ch in dic[digits[i]]:
                print(ch)
                dfs(i+1, s+ch)
        dfs(0, "")
        return res

