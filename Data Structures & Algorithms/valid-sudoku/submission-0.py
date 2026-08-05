from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        square = defaultdict(set)
        for row_idx in range(9):
            for column_idx in range(9):
                if board[row_idx][column_idx] == ".":
                    # empty sudoku
                    continue
                if (
                    board[row_idx][column_idx] in rows[row_idx]
                    or
                    board[row_idx][column_idx] in columns[column_idx]
                    or
                    board[row_idx][column_idx] in square[(row_idx //3, column_idx // 3)]
                ):
                    return False
                rows[row_idx].add(board[row_idx][column_idx])
                columns[column_idx].add(board[row_idx][column_idx])
                square[(row_idx //3, column_idx // 3)].add(board[row_idx][column_idx])

        return True