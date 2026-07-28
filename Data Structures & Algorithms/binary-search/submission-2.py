class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = start+end//2
        while start <= end:
            # print(start, end, mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid-1
                mid = (start+ end)//2
            else:
                start = start+1
                mid = (start+ end)//2
        return -1

