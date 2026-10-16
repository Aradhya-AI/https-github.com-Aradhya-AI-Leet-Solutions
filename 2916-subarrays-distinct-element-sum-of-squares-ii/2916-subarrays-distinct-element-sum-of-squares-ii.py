from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        squares = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, left, right, value):
            length = right - left + 1
            old_total = total[node]

            squares[node] = (
                squares[node]
                + 2 * value * old_total
                + value * value * length
            ) % MOD

            total[node] = (
                old_total + value * length
            ) % MOD

            lazy[node] = (lazy[node] + value) % MOD

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            value = lazy[node]

            apply(node * 2, left, mid, value)
            apply(node * 2 + 1, mid + 1, right, value)

            lazy[node] = 0

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return

            push(node, left, right)
            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)

            total[node] = (
                total[node * 2] + total[node * 2 + 1]
            ) % MOD

            squares[node] = (
                squares[node * 2] + squares[node * 2 + 1]
            ) % MOD

        last = {}
        answer = 0

        for i, num in enumerate(nums):
            start = last.get(num, -1) + 1

            update(1, 0, n - 1, start, i)

            answer = (answer + squares[1]) % MOD
            last[num] = i

        return answer