import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten, fresh = 2, 1
        freshCount = 0
        minutes = 0
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == fresh:
                    freshCount += 1
                elif grid[r][c] == rotten:
                    q.append((r, c))

        while q and freshCount > 0:
            qLen = len(q)

            for _ in range(qLen):
                r, c = q.popleft()

                for nr, nc in [
                    (r, c + 1), (r, c - 1),
                    (r + 1, c), (r - 1, c)
                ]:
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == fresh
                    ):
                        grid[nr][nc] = rotten
                        freshCount -= 1
                        q.append((nr, nc))

            minutes += 1

        return -1 if freshCount else minutes