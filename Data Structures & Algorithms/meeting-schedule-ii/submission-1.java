/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        if(intervals.size() == 0) {
            return 0;
        }
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for(int i=0; i<intervals.size(); i++) {
            min = Math.min(min, intervals.get(i).start);
            max = Math.max(max, intervals.get(i).end);
        }

        System.out.println(min+" "+ max);
        
        List<Integer> ar = new ArrayList<>(Collections.nCopies(max, 0));

        for(int i=0; i<intervals.size(); i++) {
            int start = intervals.get(i).start;
            int end = intervals.get(i).end;
            System.out.println(start+" "+ end);
            for(int j= start; j<end; j++) {
                ar.set(j, ar.get(j)+1);
            }
        }

        max = Integer.MIN_VALUE;
        for(int i=0; i<ar.size(); i++) {
            max = Math.max(max, ar.get(i));
        }
        return max;
    }
}
