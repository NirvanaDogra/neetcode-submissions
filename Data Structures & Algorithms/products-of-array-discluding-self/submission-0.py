class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsOfZero = 0
        prod = 1
        for i in nums:
            if i!=0:
                prod = prod*i
            else:
                numsOfZero+=1
        
        ar = []
        if numsOfZero == 1:
            for i in nums:
                if i == 0:
                    ar.append(prod)
                else:
                    ar.append(0)
        
        if numsOfZero == 0:
            for i in nums:
                ar.append(prod//i)

        if numsOfZero >1:
            ar = [0]*len(nums)
        return ar
        

        