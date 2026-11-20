class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxTotal = 0
        curLength = 0
        seen = set()

        def dfs(r, c):
            nonlocal curLength
            if (r < 0 or r >= rows or c < 0 or c >= cols
                    or grid[r][c] == 0 or (r, c) in seen):
                return
            seen.add((r, c))
            curLength += 1
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    curLength = 0          
                    dfs(r, c)
                    maxTotal = max(maxTotal, curLength)

        return maxTotal
        