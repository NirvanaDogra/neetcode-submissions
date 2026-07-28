class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Boolean> map = new HashMap<Integer, Boolean>();
        for(int i: nums) {
           Boolean isInMap = map.getOrDefault(i, false);
           if(isInMap) {
            return true;
           } else {
            map.put(i, true);
           }
        }
        return false;
    }
}