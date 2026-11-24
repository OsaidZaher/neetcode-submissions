class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q = deque()
        INF = 2147483647

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        dist = 0
        while q:
            dist+=1
            qLen = len(q)
            for _ in range(qLen):
                r,c = q.popleft()


                for nr,nc in [(r,c+1), (r,c-1), (r+1,c), (r-1,c)]:
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == INF:
                        grid[nr][nc] = dist
                        q.append((nr,nc))
            


        