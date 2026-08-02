class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        if (nums == null) {
            return List.of();
        }
        Arrays.sort(nums);
        // System.out.println(nums);
        List<List<Integer>> result = new ArrayList<>();
        for (int ptr1 = 0; ptr1 < nums.length; ptr1++) {
            if (nums[ptr1] > 0) break;
            if (ptr1 > 0 && nums[ptr1] == nums[ptr1 - 1]) continue;
            int ptr2 = ptr1 + 1;
            int ptr3 = nums.length - 1;
            // System.out.println(""+nums[ptr1]+""+nums[ptr2]+""+nums[ptr3]);
            while (ptr2 < ptr3) {
                int sum = nums[ptr1] + nums[ptr2] + nums[ptr3];
                // System.out.println(sum);
                if (sum == 0) {
                    result.add(List.of(nums[ptr1], nums[ptr2], nums[ptr3]));
                    ptr2++;
                    ptr3--;
                    while (ptr2 < ptr3 && nums[ptr2] == nums[ptr2 - 1]) {
                        ptr2++;
                    }
                } else if (sum < 0) {
                    ptr2++;
                } else {
                    ptr3--;
                }
            }
        }
        return result;
    }
}
