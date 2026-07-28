class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        has = False
        def dfs(i, j, matchAt):
            print(i, j)
            nonlocal has
            if matchAt == len(word):
                has = True
                return  
            if i < 0 or i>=rows:
                print("yes")
                return 
            if j< 0 or j>=cols:
                return

            if board[i][j] == word[matchAt]:
                temp = board[i][j]
                board[i][j] = '#' # mark as visited.
                dfs(i + 1, j, matchAt + 1)
                dfs(i - 1, j, matchAt + 1)
                dfs(i, j + 1, matchAt + 1)
                dfs(i, j - 1, matchAt + 1)
                board[i][j] = temp #reset the board.
                
        for i in range(0, rows):
            for j in range(0, cols):
                if board[i][j] == word[0]:
                    print(i, j)
                    dfs(i, j, 0)
                    if has:
                        return has
        return has