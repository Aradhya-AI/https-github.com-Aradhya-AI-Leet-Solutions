class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        empty = 0
        start_r = start_c = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    empty += 1
                elif grid[r][c] == 1:
                    start_r, start_c = r, c

        def dfs(r, c, remaining):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0

            if grid[r][c] == -1:
                return 0

            if grid[r][c] == 2:
                return 1 if remaining == 0 else 0

            temp = grid[r][c]
            grid[r][c] = -1

            paths = (
                dfs(r + 1, c, remaining - 1) +
                dfs(r - 1, c, remaining - 1) +
                dfs(r, c + 1, remaining - 1) +
                dfs(r, c - 1, remaining - 1)
            )

            grid[r][c] = temp
            return paths

        return dfs(start_r, start_c, empty + 1)