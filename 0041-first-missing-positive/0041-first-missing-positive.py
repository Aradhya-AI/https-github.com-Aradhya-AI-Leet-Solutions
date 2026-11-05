class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)

        num = 1

        while num in seen:
            num += 1

        return num
