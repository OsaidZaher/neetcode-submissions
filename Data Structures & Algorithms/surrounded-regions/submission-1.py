class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()

        for sr in range(rows):
            for sc in range(cols):
                if board[sr][sc] != 'O' or (sr, sc) in visited:
                    continue

                stack = [(sr, sc)]
                visited.add((sr, sc))
                region = []
                touches_edge = False

                while stack:
                    r, c = stack.pop()
                    region.append((r, c))

                    if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                        touches_edge = True

                    for nr, nc in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
                        if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                            if (nr, nc) not in visited:
                                visited.add((nr, nc))
                                stack.append((nr, nc))

                if not touches_edge:
                    for rr, cc in region:
                        board[rr][cc] = 'X'
            