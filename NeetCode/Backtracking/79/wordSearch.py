class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, wd) -> bool:
            if not len(wd):
                return True
            if (
                r < 0 or c < 0 
                or r >= row or c >= col
                or (r, c) in path
                or board[r][c] != wd[0]
            ):
                return False
            path.add((r, c))
            curr = (dfs(r - 1, c, wd[1:]) 
                    or dfs(r + 1, c, wd[1:])
                    or dfs(r, c - 1, wd[1:])
                    or dfs(r, c + 1, wd[1:]))
            path.remove((r, c))
            return curr
        
        out = False
        for i in range(row):
            for j in range(col):
                out = out or dfs(i, j, word)
        return out
              
