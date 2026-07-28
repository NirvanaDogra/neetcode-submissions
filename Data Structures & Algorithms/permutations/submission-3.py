class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def find(subset, choices):
            print(subset, choices)
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i in range(0, len(choices)):
                subset.append(choices[i])
                newChoice = choices.copy()
                newChoice.pop(i)
                find(subset, newChoice)
                subset.pop()
        find([], nums)
        return res