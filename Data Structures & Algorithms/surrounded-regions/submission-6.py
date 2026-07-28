class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = []
        rows = len(board)
        cols = len(board[0])
        visited  = set()
        
        borderO = set()

        for i in range(rows):
            if board[i][0] == "O":
                borderO.add((i, 0))
            if board[i][cols-1] == "O":
                borderO.add((i, cols-1))

        for i in range(cols):
            if board[0][i] == "O":
                borderO.add((0, i))
            if board[rows-1][i] == "O":
                borderO.add((rows-1, i))
        

        visited = set()
        def dfs(i, j):
            
            if i not in range(0, rows) or j not in range(0, cols) or (i, j) in visited:
                return
            if board[i][j] == "O":

                visited.add((i, j))
                board[i][j] = "T"
                print(i, j, board[i][j])
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
            


        for i, j in borderO:
            
            dfs(i, j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"
                


        
