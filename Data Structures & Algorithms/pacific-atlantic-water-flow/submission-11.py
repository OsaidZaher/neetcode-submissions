'''
- heights = grid where heights[r][c] == height above sea level
- pacific ocean =  top and left
- atlantic coean =  bottom and right 
- if nieghbouring cell >= current cell water can flow through
- find all cells where water can follow to each end lefft and right, top and bottom
- return the positions of all cells as a sub array in a array results


'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c, visit, prevHeight):
            
            if r< 0 or c< 0 or r== rows or c == cols or (r,c) in visit or heights[r][c] < prevHeight:
                return 
            visit.add((r,c))
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])


        for c in  range(cols):
            dfs(0,c, pac, heights[0][c])
            dfs(rows-1,c , atl, heights[rows-1][c] )
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])
        
        res = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])

        return res
        