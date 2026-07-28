class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hasTwo0 = False
        hasOne0 = False

        prodWithOut0 = 1
        for num in nums:
            if num == 0:
                if hasOne0:
                    hasTwo0 = True
                else:
                    hasOne0 = True
            else:
                prodWithOut0 *= num
        print(prodWithOut0)

        if hasTwo0:
            return [0] * len(nums)
        
        if hasOne0:
            res = [0] * len(nums)
            idx = nums.index(0)
            print(idx)
            res[idx] = prodWithOut0
            return res
        
        res =[]
        for num in nums:
            res.append(int(prodWithOut0/num))
        return res


