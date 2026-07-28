class Solution {
    List<Integer> memo = new ArrayList<Integer>();
    Integer max = Integer.MIN_VALUE;
    private int dfs(List<Integer> nums, Integer i) {
        
        if(i == nums.size()-1) {
            return 1;
        }

        int result = 1;
        for(int j=i+1; j<nums.size(); j++) {
            if(nums.get(i) < nums.get(j)) {
                System.out.println(nums.get(i)+" "+nums.get(j));
                int sresult = 1+dfs(nums, j);
               
                result = Math.max(result, sresult);
                 System.out.println("result"+ result);
            } 
        }
        max = Math.max(max, result);
        return result;
    }
    public int lengthOfLIS(int[] nums) {
        List<Integer> list = Arrays.stream(nums)
                        .boxed()
                        .collect(Collectors.toList());

        for(int j=0; j<list.size(); j++) {
            dfs(list, j);
        }
        
        return (max == -2147483648) ? 1 : max;
    }   
}
