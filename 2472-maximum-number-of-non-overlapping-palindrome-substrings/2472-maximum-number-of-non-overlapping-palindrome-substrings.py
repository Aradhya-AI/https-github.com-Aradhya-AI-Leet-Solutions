from typing import List

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        is_pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (
                    j - i < 2 or is_pal[i + 1][j - 1]
                ):
                    is_pal[i][j] = True

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):

            dp[i] = dp[i + 1]

            for j in range(i + k - 1, n):
                if is_pal[i][j]:
                    dp[i] = max(dp[i], 1 + dp[j + 1])

        return dp[0]
