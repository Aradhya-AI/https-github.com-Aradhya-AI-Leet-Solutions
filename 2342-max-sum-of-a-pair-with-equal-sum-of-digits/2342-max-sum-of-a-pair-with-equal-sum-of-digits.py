
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_digit_sum = {}
        answer = -1

        for num in nums:
            digit_sum = sum(int(d) for d in str(num))

            if digit_sum in max_digit_sum:
                answer = max(answer, num + max_digit_sum[digit_sum])

            max_digit_sum[digit_sum] = max(
                num, max_digit_sum.get(digit_sum, 0)
            )

        return answer