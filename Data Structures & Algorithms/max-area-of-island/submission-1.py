class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxCount = 0
        currCount = 0

        def dfs(r, c):
            nonlocal currCount
            if (r < 0 or r >= rows or c < 0 or c >= cols
                    or (r, c) in visit or grid[r][c] == 0):
                return

            visit.add((r, c))
            currCount += 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    currCount = 0
                    dfs(r, c)
                    maxCount = max(maxCount, currCount)

        return maxCount