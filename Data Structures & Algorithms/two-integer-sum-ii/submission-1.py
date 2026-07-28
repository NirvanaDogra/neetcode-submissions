class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1 = 0
        ptr2 = len(numbers)-1
        nums = numbers
        while ptr1<ptr2:
            if nums[ptr1] + nums[ptr2] == target:
                return [ptr1+1, ptr2+1]
            elif nums[ptr1] + nums[ptr2] > target:
                ptr2-=1
            else:
                ptr1+=1
        return []