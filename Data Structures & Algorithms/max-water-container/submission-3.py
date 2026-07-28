class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(heights) - 1
        width =  len(heights) - 1
        maxAmt = 0
        while ptr1 < ptr2:
            maxAmt = max(maxAmt, min(heights[ptr1], heights[ptr2]) * width)
            print(ptr1, ptr2, width, maxAmt)
            if heights[ptr1] > heights[ptr2]:
                ptr2-=1
            else:
                ptr1+=1
            width-=1
       
        return maxAmt

