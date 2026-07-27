class Solution:
    def isValidSudoku(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                val = board[row][col]

                # Check the row
                for c in range(9):
                    if c != col and board[row][c] == val:
                        return False

                # Check the column
                for r in range(9):
                    if r != row and board[r][col] == val:
                        return False

                # Check the 3x3 box
                start_row = (row // 3) * 3
                start_col = (col // 3) * 3

                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):
                        if (r != row or c != col) and board[r][c] == val:
                            return False

        return True