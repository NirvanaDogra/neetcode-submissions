class Solution {
    public int[] productExceptSelf(int[] nums) {
        int product = 1;
        int numberOfZero = 0;
        for(int num: nums) {
            if (num == 0) {
                numberOfZero++;
            } else  {
                product = product * num;
            }
        }


        int[] result = new int[nums.length];
        if(numberOfZero > 1) {    
            return result;
        }
        if(numberOfZero == 1) {
            for(int i=0; i<nums.length; i++) {
                if (nums[i] == 0) {
                    result[i] = product;
                    return result;
                }
            }
        }

        for(int i=0; i<nums.length; i++) {
            result[i] = product/nums[i];
        }
        return result;

    }
}