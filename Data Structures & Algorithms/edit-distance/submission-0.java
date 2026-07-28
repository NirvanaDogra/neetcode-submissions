class Solution {
    int[][] dp;
    private int dfs(String word1, String word2, int i, int j) {
        if (i == word1.length()){
            return word2.length()-j;
        } 
        if(j == word2.length()) {
            return word1.length()-i;
        }
        if (dp[i][j]!=-1) return dp[i][j];

        
        if (word1.charAt(i) == word2.charAt(j)) {
           dp[i][j] = dfs(word1, word2, i+1, j+1);
        } else {
           int insert = dfs(word1, word2, i, j+1);
            int delete = dfs(word1, word2, i+1, j);
            int replace = dfs(word1, word2, i+1, j+1);
            dp[i][j] = 1 + Math.min(Math.min(insert, delete), replace);
        }
        return dp[i][j];
    }
       

    public int minDistance(String word1, String word2) {
        dp = new int[word1.length()][word2.length()];
        for(int i=0; i<word1.length(); i++) {
            for(int j=0; j<word2.length(); j++) {
                dp[i][j] = -1;
            }
        }

        return dfs(word1, word2, 0, 0);
    }
}
