from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):
                piece = s[start:end + 1]

                if piece == piece[::-1]:
                    path.append(piece)
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return result
