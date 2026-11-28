class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set((0,0))
        q = deque([(0,0)])
        count = 1

        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1

        if rows == 1 and cols == 1:
            return 1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr,nc in  [(r+1,c), (r-1,c), (r,c+1), (r,c-1),(r+1,c-1), (r+1,c+1), (r-1,c+1), (r-1,c-1)]:
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in seen and grid[nr][nc] == 0:
                        if (nr,nc) == (rows-1, cols-1):
                            return count+1
                        seen.add((nr,nc))
                        q.append((nr,nc))
                
            count +=1

        return -1
                        

        