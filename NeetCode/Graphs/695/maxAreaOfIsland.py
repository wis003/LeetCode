class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]
        largest = 0
        curr = 0
        
        def dfs(r, c):
            nonlocal curr
            if (r < 0 or c < 0 or
                r == row or c == col or
                visited[r][c] == 1 or
                grid[r][c] == 0):
                return
            curr += 1
            visited[r][c] = 1
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        for i in range(row):
            for j in range(col):
                curr = 0
                dfs(i, j)
                if curr > largest:
                    largest = curr
        return largest