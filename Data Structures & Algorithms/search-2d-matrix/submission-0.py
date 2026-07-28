class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums) -> bool:
            start = 0
            end = len(nums)-1
            mid = start+end//2
            while start <= end:
                # print(start, end, mid)
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    end = mid-1
                    mid = (start+ end)//2
                else:
                    start = start+1
                    mid = (start+ end)//2
            return False
        
        for row in matrix:
            if search(row): return True
        return False