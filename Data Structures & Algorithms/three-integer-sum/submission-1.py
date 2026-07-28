class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        bigAr=[]
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ptr1 = i+1
            ptr2 = len(nums)-1 
            while ptr1<ptr2:
                if nums[i]+nums[ptr1] + nums[ptr2] == 0:
                    bigAr.append([nums[i], nums[ptr1], nums[ptr2]])
                    ptr1+=1
                    ptr2-=1
                    while ptr1 < ptr2 and nums[ptr1] == nums[ptr1 - 1]:
                        ptr1 += 1
                    while ptr1 < ptr2 and nums[ptr2] == nums[ptr2 + 1]:
                        ptr2 -= 1

                elif nums[i]+nums[ptr1] + nums[ptr2] > 0:
                    ptr2-=1
                else:
                    ptr1+=1
        return bigAr