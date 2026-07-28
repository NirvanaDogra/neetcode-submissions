class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(ar, target):
            s = 0
            e = len(ar)-1
            while s<=e:
                m = (s+e)//2

                if target<ar[m]:
                    e = m-1
                elif target > ar[m]:
                    s = m+1
                else: 
                    return m
            return -1
        
        for ar in matrix:
            pos = search(ar, target)
            if pos != -1:
                return True
        return False