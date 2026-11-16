class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        seen = set()
        numIslands = 0

        def dsf(r,c):

            if 0 > r or r >= rows or c<0 or c>= cols or grid[r][c] =='0' or (r,c) in seen:
                return 

            else:

                seen.add((r,c))

                dsf(r, c+1)
                dsf(r, c-1)
                dsf(r+1, c)
                dsf(r-1, c)





        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in seen:
                    dsf(i, j)
                    numIslands+=1


        return numIslands