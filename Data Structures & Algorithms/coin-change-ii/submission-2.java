class Solution {
    private final Map<String, Integer> memo = new HashMap<>();

    private int dfs(int amount, int[] coins, int pos) {
        if (amount == 0) return 1;
        if (amount < 0 || pos == coins.length) return 0;

        String key = amount + "-" + pos;
        if (memo.containsKey(key)) return memo.get(key);

        // Option 1: pick current coin
        int include = dfs(amount - coins[pos], coins, pos);

        // Option 2: skip current coin
        int exclude = dfs(amount, coins, pos + 1);

        int total = include + exclude;
        memo.put(key, total);
        return total;
    }

    public int change(int amount, int[] coins) {
        return dfs(amount, coins, 0);
    }
}
