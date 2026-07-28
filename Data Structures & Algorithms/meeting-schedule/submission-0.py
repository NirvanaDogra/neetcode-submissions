"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ar = []
        for i in range(0, 1000000):
            ar.append(0)

        for i in intervals:
            for j in range(i.start, i.end):
                ar[j]+=1
                if ar[j] > 1:
                    return False
        
        return True