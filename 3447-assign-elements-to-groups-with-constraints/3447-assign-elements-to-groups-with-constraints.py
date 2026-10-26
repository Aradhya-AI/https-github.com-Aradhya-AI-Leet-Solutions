
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        mx = max(groups)
        index = [-1] * (mx + 1)

        for j, x in enumerate(elements):
            if x > mx or index[x] != -1:
                continue

            for multiple in range(x, mx + 1, x):
                if index[multiple] == -1:
                    index[multiple] = j

        return [index[g] for g in groups]
