'''
you are given an 2D array of values 

each cell has one of either elements

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit

at every iteration the cell with val1 become val2 if beside val1
return total minutes before all fruits become 2 else return -1


--

approach:


find the total of count of fresh fruit if not empty return -1
create a q to add rotten values in
when there is current rotten fruit in q move to its neighbours and check if they are also rotten, if not rotten make them into rotten, repeat layer by layer 


'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        empty, fresh, rotten = 0,1,2
        q = collections.deque()
        freshCount = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == rotten:
                    q.append((r,c))
                elif  grid[r][c] == fresh:
                    freshCount +=1
        
        while q and freshCount:
            qLen = len(q)
            for _ in range(qLen):
                r,c = q.popleft()
                for nr,nc in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == fresh:
                        grid[nr][nc] = rotten
                        q.append((nr,nc))
                        freshCount -=1
            minutes +=1

        return minutes if not freshCount else -1

        