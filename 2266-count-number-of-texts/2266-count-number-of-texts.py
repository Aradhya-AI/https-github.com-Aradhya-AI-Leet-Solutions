class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10**9 + 7
        n = len(pressedKeys)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            limit = 4 if pressedKeys[i - 1] in "79" else 3

            for length in range(1, limit + 1):
                if i - length < 0:
                    break

                if len(set(pressedKeys[i - length:i])) == 1:
                    dp[i] = (dp[i] + dp[i - length]) % MOD
                else:
                    break

        return dp[n]
