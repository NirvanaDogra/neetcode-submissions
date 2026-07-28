class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res  = []
        def dfs(i, ar):
            if i == len(nums):
                res.append(ar.copy())
                return 
            ar.append(nums[i])
            print(ar)
            dfs(i+1, ar)
            ar.remove(nums[i])
            dfs(i+1, ar)
        dfs(0, [])
        return res


        



        