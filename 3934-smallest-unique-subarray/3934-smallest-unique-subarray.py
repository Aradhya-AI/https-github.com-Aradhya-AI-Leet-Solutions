class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        vals = {v: i for i, v in enumerate(sorted(set(nums)))}
        rank = [vals[x] for x in nums]

        sa = list(range(n))
        k = 1

        while k < n:
            sa.sort(key=lambda i: (
                rank[i],
                rank[i + k] if i + k < n else -1
            ))

            new_rank = [0] * n

            for i in range(1, n):
                a, b = sa[i - 1], sa[i]

                prev = (rank[a], rank[a + k] if a + k < n else -1)
                curr = (rank[b], rank[b + k] if b + k < n else -1)

                new_rank[b] = new_rank[a] + (prev != curr)

            rank = new_rank

            if rank[sa[-1]] == n - 1:
                break

            k *= 2

        lcp = [0] * n
        pos = [0] * n

        for i in range(n):
            pos[sa[i]] = i

        h = 0

        for i in range(n):
            r = pos[i]

            if r == 0:
                continue

            j = sa[r - 1]

            while i + h < n and j + h < n and nums[i + h] == nums[j + h]:
                h += 1

            lcp[r] = h

            if h:
                h -= 1

        ans = n

        for r in range(n):
            i = sa[r]

            longest = lcp[r]

            if r + 1 < n:
                longest = max(longest, lcp[r + 1])

            length = longest + 1

            if length <= n - i:
                ans = min(ans, length)

        return ans