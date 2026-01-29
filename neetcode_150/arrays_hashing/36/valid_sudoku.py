#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# logic: iterate through each row, column, and segment, checking for duplicates

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        blocks = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if board[r][c] == ".":
                    continue

                block = (r // 3)*3 + (c // 3)

                if cell in rows[r] or cell in cols[c] or cell in blocks[block]:
                    return False
                else:
                    rows[r].add(cell)
                    cols[c].add(cell)
                    blocks[block].add(cell)

        return True