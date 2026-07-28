class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i=0;i<nums.length; i++) {
            if(!map.containsKey(nums[i])) {
                map.put(target-nums[i], i);
            } else {
                int x = map.get(nums[i]);
                return new int[] {x, i};
            }
            System.out.println(map);
        }
        return new int[] {};
    }
}
