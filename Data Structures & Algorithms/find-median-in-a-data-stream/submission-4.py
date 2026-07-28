class MedianFinder:

    def __init__(self):
        self.ar =[]

    def addNum(self, num: int) -> None:
        isInserted = False
        for i in range(0, len(self.ar)):
            if num <= self.ar[i]:
                self.ar.insert(i, num)
                isInserted = True
                break
        if not isInserted:
            self.ar.append(num)
        print(self.ar)

    def findMedian(self) -> float:
        size = len(self.ar)
        if size % 2 == 0:
            return (self.ar[size//2 -1]+self.ar[size//2])/2.0
        else:
            return self.ar[size//2]
        
        