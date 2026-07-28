class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        res = set()
        def dfs(subset, i):
            if sum(subset) == target:
                res.add(tuple(sorted(subset.copy())))
            
            if i == len(nums) or sum(subset) > target:
                return
           

            subset.append(nums[i])
        
            dfs(subset, i+1)
            subset.pop()
            dfs(subset, i+1)

        dfs([], 0)
        return [list(sub) for sub in res]
            