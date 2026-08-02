class Solution {
    public int maxArea(int[] heights) {
        // max(w * min(h1, h2))
        int h1 = 0;
        int h2 = heights.length - 1;
        int maxWater = 0;
        while(h1 < h2) {
            int width = h2-h1;
            maxWater = Math.max(maxWater, width * Math.min(heights[h1], heights[h2]));
            if(heights[h1] < heights[h2]) {
                h1++;
            } else if(heights[h1] > heights[h2]) {
                h2--;
            } else {
                h1++;
                h2--;
            }
        }
        return maxWater;
    }
}
