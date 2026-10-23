from collections import Counter
from typing import List

class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        ans = 0
        same = 0
        freq = Counter()

        for i in range(n):
            if nums1[i] == nums2[i]:
                ans += i
                same += 1
                freq[nums1[i]] += 1 

        max_freq = max(freq.values(), default=0)
        dominant = next(
            (x for x, count in freq.items() if count == max_freq),
            -1
        )

        need = max(0, 2 * max_freq - same)

        for i in range(n):
            if need == 0:
                break

            if (nums1[i] != nums2[i]
                    and nums1[i] != dominant
                    and nums2[i] != dominant):
                ans += i
                need -= 1

        return ans if need == 0 else -1
