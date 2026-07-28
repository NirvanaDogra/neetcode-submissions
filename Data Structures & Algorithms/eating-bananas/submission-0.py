class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxRate = max(piles)
        
        start = 1
        end = maxRate
        minRate = maxRate+1
        while start<=end:
            mid = (start+end)//2
            print(mid, [math.ceil(float(n) / mid) for n in piles])
            rate = sum([math.ceil(float(n) / mid) for n in piles])
            print(rate)
            if rate <= h:
                minRate = min(minRate, mid)
                end = mid -1
            else:
                start = mid+1
        return minRate
           