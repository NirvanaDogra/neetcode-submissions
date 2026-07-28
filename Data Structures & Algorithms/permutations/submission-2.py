class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(subset):
            if len(subset) == 0:
                return [[]]
            perms = dfs(subset[1:])
            print(perms, subset[0] )

            moreP = []
            for p in perms:
                for i in range(0, len(p)+1):
                    curr = p.copy()
                    curr.insert(i, subset[0])
                    moreP.append(curr)
            return moreP
        
        return dfs(nums)
            


