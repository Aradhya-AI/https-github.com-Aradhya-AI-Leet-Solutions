class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(word) for word in s.split() if word.isdigit()]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return False

        return True