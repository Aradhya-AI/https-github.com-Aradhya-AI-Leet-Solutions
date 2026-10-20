
from typing import List
from math import isqrt

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)

        qelvarodin = nums[:]

        def can_sort(k):
            previous_max = None

            for start in range(0, n, k):
                end = start + k
                minimum = min(qelvarodin[start:end])
                maximum = max(qelvarodin[start:end])

                descents = 0

                for i in range(start, end):
                    next_i = start if i == end - 1 else i + 1

                    if qelvarodin[i] > qelvarodin[next_i]:
                        descents += 1

                if descents > 1:
                    return False

                if (previous_max is not None
                        and previous_max > minimum):
                    return False

                previous_max = maximum

            return True

        answer = 0

        for d in range(1, isqrt(n) + 1):
            if n % d == 0:
                if can_sort(d):
                    answer += d

                other = n // d

                if other != d and can_sort(other):
                    answer += other

        return answer
