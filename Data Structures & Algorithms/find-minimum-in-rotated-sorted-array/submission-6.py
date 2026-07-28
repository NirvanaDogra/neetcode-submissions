class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        minVal = 99999
        while start <= end:
            mid = (start+end)//2
            minVal = min(minVal, nums[mid])
            if nums[start] < nums[mid]:
                if nums[mid] > nums[end]:
                    start = mid+1
                else:
                    end = mid -1
            else:
                if nums[mid] < nums[end]:
                    end = mid-1
                else:
                    start = mid+1
        return minVal