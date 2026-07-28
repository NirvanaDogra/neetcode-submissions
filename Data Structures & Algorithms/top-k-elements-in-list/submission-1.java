class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<List<Integer>> ar = new ArrayList<>(nums.length);
        HashMap<Integer, Integer> map = new HashMap<>();

        // { number: freq}
        for(int i=0; i<nums.length; i++) {
            Integer updatedVal = map.getOrDefault(nums[i], 0)+1;
            map.put(nums[i], updatedVal);
        }

        for(int i=0; i<=nums.length; i++) {
            ar.add(new ArrayList<Integer>());
        }

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int num = entry.getKey();
            int freq = entry.getValue();
            ar.get(freq).add(num);
            System.out.println("adding " + freq + " -> " + num);
        }

        int[] res = new int[k];
        int count =0;
        for(int i=nums.length; i>=0; i--) {
            for(int frqNum: ar.get(i)) {
                System.out.println("fre"+ frqNum);
                res[count++] = frqNum;
                if (count == k) {
                    return res;
                }
            }
        }
        return res;

        

    }
}
