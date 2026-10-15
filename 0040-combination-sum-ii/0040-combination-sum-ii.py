
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                num = candidates[i]

                # No need to check larger numbers
                if num > remaining:
                    break

                path.append(num)

                # Each element can be used only once
                backtrack(i + 1, remaining - num)

                # Undo the choice
                path.pop()

        backtrack(0, target)
        return result