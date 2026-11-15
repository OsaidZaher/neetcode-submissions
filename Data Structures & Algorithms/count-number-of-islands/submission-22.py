class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        numIslands = 0
        seen = set()

        def dfs(r,c):

            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == '0' or (r,c) in seen:
                return
            else:

                seen.add((r,c))
                dfs(r, c+1)
                dfs(r, c-1)
                dfs(r+1, c)
                dfs(r-1, c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in seen:
                    numIslands +=1
                    dfs(r,c)
        
        return numIslands