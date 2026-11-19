'''
- given a matrix 
- if a cell == 0 rows and cols == 0
- update the matrix in place

--

Input: matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]

iterate over every row and every column if cell == 0 make row and cols == 0
do this in another array 

--



'''



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS, COLS = len(matrix), len(matrix[0])
        rows, cols = [False] *len(matrix),  [False] * len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True

        for r in range(ROWS):
            for c in range(COLS):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0
            




        
        