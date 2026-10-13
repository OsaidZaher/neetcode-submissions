class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(len(board)):
            currentSet = set()

            for col in range(len(board[0])):
                value = board[row][col]

                if value == '.':
                    continue

                if value in currentSet:
                    return False

                currentSet.add(value)

        for col in range(len(board[0])):
            currentSet = set()

            for row in range(len(board)):
                value = board[row][col]

                if value == '.':
                    continue

                if value in currentSet:
                    return False

                currentSet.add(value)

        for start_row in range(0, len(board), 3):
            for start_col in range(0, len(board[0]), 3):

                currentSet = set()

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):

                        value = board[row][col]

                        if value == '.':
                            continue

                        if value in currentSet:
                            return False

                        currentSet.add(value)

        return True