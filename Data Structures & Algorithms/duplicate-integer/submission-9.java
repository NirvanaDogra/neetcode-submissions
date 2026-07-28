class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Boolean> map = new HashMap<Integer, Boolean>();
        for(int i: nums) {
            if(map.containsKey(i)) {
                return true;
            }
            map.put(i, true);
        }
        return false;
    }
}