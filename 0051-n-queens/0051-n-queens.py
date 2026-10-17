from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        diagonals1 = set()
        diagonals2 = set()

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if (
                    col in cols
                    or (row + col) in diagonals1
                    or (row - col) in diagonals2
                ):
                    continue

                board[row][col] = "Q"
                cols.add(col)
                diagonals1.add(row + col)
                diagonals2.add(row - col)

                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diagonals1.remove(row + col)
                diagonals2.remove(row - col)

        backtrack(0)
        return result