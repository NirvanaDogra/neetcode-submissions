class Solution {
    HashMap<String, Integer> map = new HashMap<String, Integer>();
    private int dfs(int[] nums, int target, int i) {
        System.out.println(i);
        String key = i+"-"+target;
        if(target == 0 && i==nums.length) {return 1;}
        if (target != 0 && i>=nums.length) {return 0;} 
        if (map.containsKey(key)) {return map.get(key);}

        int result = 0;
        result += dfs(nums, target+nums[i], i+1);
        result += dfs(nums, target-nums[i], i+1);
        map.put(key, result);
        return result;
    }
    public int findTargetSumWays(int[] nums, int target) {
        return dfs(nums, target, 0) ;
    }
}
