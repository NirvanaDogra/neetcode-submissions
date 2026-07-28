class Solution {
    int numberOfPath = 0;
    private void dfs(int i, int j, int m, int n){
        System.out.println(""+i+" "+j);
        if (i == m && j == n) {
            numberOfPath+=1;
            return;
        }
        if(i == m && j<n) {
            dfs(i, j+1, m, n);
        }
        else if(j == n && i<m) {
            dfs(i+1, j, m, n);
        }
        else {
            dfs(i, j+1, m, n);
            dfs(i+1, j, m, n);
        }
        
    }
    public int uniquePaths(int m, int n) {
        dfs(0, 0, m-1, n-1);
        return numberOfPath;
    }
}
