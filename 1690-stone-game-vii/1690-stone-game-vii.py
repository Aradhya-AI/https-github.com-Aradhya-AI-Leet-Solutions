class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                left = prefix[j + 1] - prefix[i + 1] - dp[i + 1][j]
                right = prefix[j] - prefix[i] - dp[i][j - 1]

                dp[i][j] = max(left, right)

        return dp[0][n - 1]