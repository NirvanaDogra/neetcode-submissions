class Solution {
    int numberOfPath = 0;
    HashMap<Pair, Integer> memo = new HashMap<Pair, Integer>();
    private int dfs(int i, int j, int m, int n){
 
        Pair pair = new Pair(i, j);
        if(memo.containsKey(pair)) {
            return memo.get(pair);
        }
        if (i == m && j == n) { 
            return 1;
        }
        if(i == m && j<n) {
            int result = dfs(i, j+1, m, n);
            memo.put(pair, result);
            return result;
        }
        else if(j == n && i<m) {
            int result = dfs(i+1, j, m, n);
            memo.put(pair, result);
            return result;
        }
        else {
            int result = dfs(i, j+1, m, n) + dfs(i+1, j, m, n);
            memo.put(pair, result);
            return result;
        }
    }
    public int uniquePaths(int m, int n) {
        return dfs(0, 0, m-1, n-1);
    }
}
