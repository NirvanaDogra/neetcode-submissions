class Solution {
    private boolean dfs(int i, int j, String s1, String s2, String s3) {

        if (i+j == s3.length()) {
            return true;
        }


        boolean first = false;
        boolean second = false;
        if(i < s1.length() && s1.charAt(i) == s3.charAt(i+j)) {
            first = dfs(i+1, j, s1, s2, s3);
        }
        if (j < s2.length() && s2.charAt(j) == s3.charAt(i+j)) {
            second = dfs(i, j+1, s1, s2, s3);
        }
        return first || second;
    }
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length()) return false;

        return  dfs(0, 0, s1, s2, s3);
    }
}
