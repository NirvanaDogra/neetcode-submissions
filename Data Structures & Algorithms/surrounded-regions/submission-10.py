class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        def dfs(i, j): 
            if (i not in range(len(board)) or
                j not in range(len(board[0])) or (i, j) in visited) :
                return
            
            if (board[i][j] == "O"):
                visited.add((i, j))
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

        for col in range(len(board[0])):
            if board[0][col] == "O":
                dfs(0, col)
            if board[len(board)-1][col] == "O":
                dfs(len(board)-1, col)
        
        for row in range(len(board)):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][len(board[0])-1] == "O":
                dfs(row, len(board[0])-1)
        

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r,c) not in visited and board[r][c] == "O":
                    board[r][c] = "X"
        