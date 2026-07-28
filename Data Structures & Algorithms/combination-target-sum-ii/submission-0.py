class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        lst = []
        
        nums = sorted(candidates)
        def dfs(i, curr):
            if i > len(nums)-1:
                if sum(curr) == target:
                    lst.append(curr)
                return
            
      
            curr.append(nums[i])

            dfs(i+1, curr.copy())
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i+1, curr.copy())
        dfs(0, [])
        return lst
        