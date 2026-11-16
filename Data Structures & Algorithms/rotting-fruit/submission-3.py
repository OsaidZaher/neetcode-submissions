import collections


'''
assign values to 0,1,2
create a for loop which checks the count of freh fruits and the count of bad fruits are added to the q

while the q exists
find the length of the q
iterate of the length of the q
popleft and get the values 

these values are checked against every position
check that the conditions are correct
change r,c to rotten
decrement freshcount 
outside loop increment minutes


'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        empty, fresh, rotten = 0,1,2
        q = collections.deque()
        minutes = 0
        freshCount = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == fresh:
                    freshCount +=1
                if grid[r][c] == rotten:
                    q.append((r,c))

        while q and freshCount > 0:
            qLen = len(q)
            for _ in range(qLen):
                r,c = q.popleft()
                for nr, nc in [(r,c+1), (r,c-1), (r+1,c), (r-1,c)]:
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == fresh:
                        freshCount -=1
                        grid[nr][nc] = rotten
                        q.append((nr,nc))
            minutes +=1

        return -1 if freshCount else minutes
        