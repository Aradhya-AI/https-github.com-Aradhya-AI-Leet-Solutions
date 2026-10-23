from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        nums.sort(key=lambda x: (freq[x], -x))

        return nums
