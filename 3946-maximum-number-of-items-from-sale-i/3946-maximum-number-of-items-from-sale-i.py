class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        cheapest = min(price for factor, price in items)

        valmorendi = (items, budget)

        free = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]
            gain = free[i] + 1

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + gain)

        ans = 0

        for b in range(budget + 1):
            ans = max(ans, dp[b] + (budget - b) // cheapest)

        return ans