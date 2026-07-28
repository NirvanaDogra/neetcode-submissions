class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [height[0]]
        rightMax = [height[-1]]

        for i in range(1, len(height)):
            leftMax.append(max(leftMax[-1], height[i]))
            rightMax.append(max(rightMax[-1], height[-1-i]))
        rightMax=rightMax[::-1]
        print(leftMax, rightMax)

        water = []

        for i in range(0, len(height)):
            water.append( min(leftMax[i], rightMax[i]) - height[i])
        print(water)
        return sum(water)
