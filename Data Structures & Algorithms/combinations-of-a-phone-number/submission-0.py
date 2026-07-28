class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lst = [
            [], ['a', 'b', 'c'], 
            ['d', 'e', 'f'], ['g', 'h', 'i'], 
            ['j', 'k', 'l'], ['m','n', 'o'], 
            ['p','q','r','s'],['t','u', 'v'], 
            ['w', 'x', 'y','z']
        ]

        print(lst)

        result = []
        def dfs(index, curr):
            if index >= len(digits):
                if curr!= "":
                    result.append(curr)
                return 
            
            char = int(digits[index])-1
            print(char+1, lst[char])

            for option in lst[char]:
                curr+=option
                dfs(index+1, curr)
                curr = curr[0:len(curr)-1]
        dfs(0, "")
        return result


       