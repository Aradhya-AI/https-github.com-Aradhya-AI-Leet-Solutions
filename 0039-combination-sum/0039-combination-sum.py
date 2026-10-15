from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > remaining:
                    break

                path.append(num)

                backtrack(i, remaining - num)

                path.pop()

        backtrack(0, target)
        return result