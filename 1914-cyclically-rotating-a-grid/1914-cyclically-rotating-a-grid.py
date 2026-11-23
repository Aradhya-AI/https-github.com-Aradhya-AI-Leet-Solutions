class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = [row[:] for row in grid]

        for layer in range(min(m, n) // 2):
            cells = []

            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer

            for j in range(left, right + 1):
                cells.append(grid[top][j])

            for i in range(top + 1, bottom + 1):
                cells.append(grid[i][right])

            for j in range(right - 1, left - 1, -1):
                cells.append(grid[bottom][j])

            for i in range(bottom - 1, top, -1):
                cells.append(grid[i][left])

            length = len(cells)
            shift = k % length
            cells = cells[shift:] + cells[:shift]

            idx = 0

            for j in range(left, right + 1):
                result[top][j] = cells[idx]
                idx += 1

            for i in range(top + 1, bottom + 1):
                result[i][right] = cells[idx]
                idx += 1

            for j in range(right - 1, left - 1, -1):
                result[bottom][j] = cells[idx]
                idx += 1

            for i in range(bottom - 1, top, -1):
                result[i][left] = cells[idx]
                idx += 1

        return result