class Solution:
    def climbStairs(self, n: int) -> int:
        ar = [0, 1, 2]

        for i in range(3, n+1):
            ar.append(ar[i-1]+ ar[i-2])
        
        return ar[n]

             