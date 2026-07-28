class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        has = False

        def dfs(i, j, matchAt):
            nonlocal has  # Declare 'has' as nonlocal

            if matchAt == len(word):
                has = True
                return
            if i < 0 or i >= rows:
                return
            if j < 0 or j >= cols:
                return

            if board[i][j] == word[matchAt]:
                temp = board[i][j]
                board[i][j] = '#' # mark as visited.
                dfs(i + 1, j, matchAt + 1)
                dfs(i - 1, j, matchAt + 1)
                dfs(i, j + 1, matchAt + 1)
                dfs(i, j - 1, matchAt + 1)
                board[i][j] = temp #reset the board.
            
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    dfs(row, col, 0)
                    if has:
                        return True
        return has