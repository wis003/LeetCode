class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        
        def dfs(r, c):
            if (
                r < 0 or c < 0
                or r == row or c == col
                or grid[r][c] == '0'
                or visited[r][c]
            ):
                return
            
            visited[r][c] = True
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        out = 0
        for i in range(row):
            for j in range(col):
                if not visited[i][j] and grid[i][j] == '1':
                    # print(i, j)
                    out += 1
                    dfs(i, j)
        return out
        
