class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        even = float('-inf')
        odd = float('-inf')

        if nums[0] % 2 == 0:
            even = nums[0]
        else:
            odd = nums[0]

        for num in nums[1:]:
            if num % 2 == 0:
                even = max(even + num, odd - x + num)
            else:
                odd = max(odd + num, even - x + num)

        return max(even, odd)