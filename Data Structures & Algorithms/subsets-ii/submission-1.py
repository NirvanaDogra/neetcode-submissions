class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lst = []
        def dfs(i, curr):
            if i > len(nums)-1:
                if sorted(curr) not in lst:
                    lst.append(sorted(curr))
                print(lst)
                return
            
      
            curr.append(nums[i])
            dfs(i+1, curr.copy())
            curr.pop()

            dfs(i+1, curr.copy())
        dfs(0, [])
        return lst
        
