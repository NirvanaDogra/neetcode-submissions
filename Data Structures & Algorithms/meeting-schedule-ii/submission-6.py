"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        if len(intervals) == 0:
            return 0
        days = [[[intervals[0].start, intervals[0].end]]]

        for interval in intervals[1:]:
            addDay = True
            for meetings in days:
                print(meetings, interval.start)
                if interval.start >= meetings[-1][1]:
                    print("appending", interval.start)
                    meetings.append([interval.start, interval.end])
                    addDay = False
                    break
            print("done", addDay)
            if addDay:
                print("adding")
                days.append([[interval.start, interval.end]])
                
        print(days)
        return len(days)
            

