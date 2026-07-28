class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(heights)-1
        maxWater = 0
        while ptr1<ptr2:
            width = ptr2-ptr1
            height = min(heights[ptr2], heights[ptr1])
            maxWater = max(maxWater, height*width)
            if heights[ptr2] > heights[ptr1]:
                ptr1+=1
            elif heights[ptr2] == heights[ptr1]:
                ptr1+=1
                ptr2-=1
            else:
                ptr2-=1



        return maxWater