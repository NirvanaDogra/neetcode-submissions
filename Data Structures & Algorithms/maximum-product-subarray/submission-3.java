class Solution {
    public int maxProduct(int[] nums) {
        int max = 1;
        int min = 1;
        int res = nums[0];
        for(int num: nums) {
            int temp = max*num;
            max = Math.max(temp, Math.max(num*min, num));
            min = Math.min(temp, Math.min(num*min, num));
            res = Math.max(res, max);
            System.out.println(max + " "+ min+ " "+ res);
        }
        return res;
    }
}
