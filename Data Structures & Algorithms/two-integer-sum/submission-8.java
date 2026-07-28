class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> posTracker = new HashMap<Integer, Integer>();
        
    
        for(int idx = 0; idx < nums.length; idx++) {
            int diff = target - nums[idx];
            if(posTracker.containsKey(nums[idx])) {
                return new int[] {posTracker.get(nums[idx]), idx};
            }
            posTracker.put(diff, idx);
        }
        return new int[]{};
    }
}
