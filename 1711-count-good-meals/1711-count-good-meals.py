class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        counts = {}
        result = 0

        for num in deliciousness:
            for power in range(22):
                target = (1 << power) - num
                result += counts.get(target, 0)

            counts[num] = counts.get(num, 0) + 1

        return result % MOD
