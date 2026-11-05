class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        result = []

        for num in range(min(nums), max(nums) + 1):
            if num not in seen:
                result.append(num)

        return result
