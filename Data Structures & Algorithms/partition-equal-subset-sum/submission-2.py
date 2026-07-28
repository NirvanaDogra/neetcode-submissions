class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        res = []
        def dfs(target, i, path):
            print(target, i, path)
            if target == 0:
                res.append(path.copy())
                return True
            if target < 0 or i>len(nums)-1:
                return False
            
            if (dfs(target-nums[i], i+1, path+[nums[i]]) or
                dfs(target, i+1, path)):
                return True
            return False

        if target% 2 != 0: return False
        c = dfs(target//2, 0, [])
        print(res)
        return c
