class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lst = []
        nums = sorted(nums)
        def dfs(i, curr):
            if i > len(nums)-1:
                if curr not in lst:
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
        
