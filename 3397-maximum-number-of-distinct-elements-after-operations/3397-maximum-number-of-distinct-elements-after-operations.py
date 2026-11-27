class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        last = float('-inf')
        ans = 0

        for num in nums:
            current = max(num - k, last + 1)

            if current <= num + k:
                ans += 1
                last = current

        return ans