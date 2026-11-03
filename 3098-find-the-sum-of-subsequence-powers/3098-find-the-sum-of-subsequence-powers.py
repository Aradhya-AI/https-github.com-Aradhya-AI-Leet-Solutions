from functools import cache
from math import inf

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        @cache
        def dfs(i, j, remaining, minimum):
            if i == n:
                return minimum if remaining == 0 else 0

            if n - i < remaining:
                return 0

            ans = dfs(i + 1, j, remaining, minimum)

            if j == n:
                ans += dfs(i + 1, i, remaining - 1, minimum)
            else:
                new_minimum = min(minimum, nums[i] - nums[j])
                ans += dfs(i + 1, i, remaining - 1, new_minimum)

            return ans % MOD

        return dfs(0, n, k, inf)
