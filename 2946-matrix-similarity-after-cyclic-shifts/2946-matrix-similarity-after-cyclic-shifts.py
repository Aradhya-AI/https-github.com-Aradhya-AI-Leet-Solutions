from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows = len(mat)
        cols = len(mat[0])

        k = k % cols

        for i in range(rows):
            for j in range(cols):
                if i % 2 == 0:
                    shifted_col = (j + k) % cols
                else:
                    shifted_col = (j - k) % cols

                if mat[i][j] != mat[i][shifted_col]:
                    return False

        return True