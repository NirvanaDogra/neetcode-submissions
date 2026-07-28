class Solution {
    private int dfs(int i, int j, int pre, int rows, int cols, int[][] matrix) {
        System.out.println(i+" "+j+" "+ pre);
        if(i < 0 || i >= rows || j<0 || j>= cols) {
            return 0;
        }
        if (matrix[i][j] > pre) {
            int curr = matrix[i][j];
            matrix[i][j] = (int) -1e9;
            int up = 1+dfs(i+1, j, curr, rows, cols, matrix);
            int down = 1+dfs(i-1, j, curr, rows, cols, matrix);
            int right = 1+dfs(i, j+1, curr, rows, cols, matrix);
            int left = 1+dfs(i, j-1, curr, rows, cols, matrix);
            matrix[i][j] = curr;
            return Math.max(up, Math.max(down, Math.max(right, left)));
        }
        return 0;
    }
    public int longestIncreasingPath(int[][] matrix) {
        int max = 0;
        for(int i =0; i<matrix.length; i++) {
            for(int j=0; j<matrix[0].length; j++) {
                max = Math.max(max, dfs(i, j, -1, matrix.length, matrix[0].length, matrix));
            }
        }
        return max;
    }
}
