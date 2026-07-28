class Solution {
    private Map<Integer, Integer> calculateFrequency(int[] nums) {
        Map<Integer, Integer> freqCountMap = new HashMap<>();
        for (int num : nums) {
            freqCountMap.put(num, freqCountMap.getOrDefault(num, 0) + 1);
        }
        return freqCountMap; 
    }

    public int[] topKFrequent(int[] nums, int k) {
        List<Integer>[] freqArray = new ArrayList[nums.length + 1];
        for (int i = 0; i <= nums.length; i++) {
            freqArray[i] = new ArrayList<>();
        }
        Map<Integer, Integer> freqCountMap = calculateFrequency(nums);
        for (Map.Entry<Integer, Integer> entry : freqCountMap.entrySet()) {
            int num = entry.getKey();
            int freq = entry.getValue();
            freqArray[freq].add(num);
        }

        int[] result = new int[k];
        int ptr = 0;

        for (int i = freqArray.length - 1; i >= 0; i--) {
            for (int num : freqArray[i]) {
                result[ptr++] = num;
                if (ptr == k) {
                    return result;
                }
            }
        }
        return result;
    }
}
