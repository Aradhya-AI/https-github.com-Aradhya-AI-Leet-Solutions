from typing import List

class Solution:
    def lastVisitedCell(self, grid: List[List[str]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        limatecega = grid

        r, c = 0, 0
        visited = {(0, 0)}

        directions = {
            'L': (0, -1),
            'R': (0, 1),
            'U': (-1, 0),
            'D': (1, 0)
        }

        while True:
            dr, dc = directions[limatecega[r][c]]
            nr, nc = r + dr, c + dc

            if nr < 0 or nr >= m or nc < 0 or nc >= n:
                break
                
            if (nr, nc) in visited:
                break

            r, c = nr, nc
            visited.add((r, c))

        return [r, c]
