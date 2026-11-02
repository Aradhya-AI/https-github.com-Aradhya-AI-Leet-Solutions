class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        dug = set(map(tuple, dig))
        result = 0

        for r1, c1, r2, c2 in artifacts:
            complete = True

            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if (r, c) not in dug:
                        complete = False
                        break

                if not complete:
                    break

            if complete:
                result += 1

        return result
