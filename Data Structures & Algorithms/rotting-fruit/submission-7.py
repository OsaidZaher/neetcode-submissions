from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        minutes = 0
        empty, fresh, rotten = 0, 1, 2
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == fresh:
                    fresh_count += 1
                elif grid[r][c] == rotten:
                    q.append((r, c))

        while q and fresh_count:
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == fresh:
                        grid[nr][nc] = rotten
                        fresh_count -= 1
                        q.append((nr, nc))
            minutes += 1

        return minutes if not fresh_count else -1