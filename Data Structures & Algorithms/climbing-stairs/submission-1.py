class Solution:
    def climbStairs(self, n: int) -> int:
        z = 1
        o = 1
        for i in range(2, n+1):
            temp = z+o
            z = o
            o = temp
        return o
        