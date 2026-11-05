class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {person: i for i, person in enumerate(row)}
        swaps = 0

        for i in range(0, len(row), 2):
            partner = row[i] ^ 1

            if row[i + 1] != partner:
                other = row[i + 1]

                row[i + 1], row[pos[partner]] = partner, other

                pos[other] = pos[partner]
                pos[partner] = i + 1

                swaps += 1

        return swaps
