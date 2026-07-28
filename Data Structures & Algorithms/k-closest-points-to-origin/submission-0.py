class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dsts = [[(i*i + j*j)**0.5, i, j] for i, j in points ]

        print(dsts)
        heapq.heapify(dsts)
        res= []
        for i in range(0, k):
            dist, x, y = heapq.heappop(dsts)
            res.append([x, y])
        
        return res