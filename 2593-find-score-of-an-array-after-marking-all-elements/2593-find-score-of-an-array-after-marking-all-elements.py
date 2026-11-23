class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n
        score = 0

        for i in sorted(range(n), key=lambda i: (nums[i], i)):
            if not marked[i]:
                score += nums[i]
                marked[i] = True

                if i > 0:
                    marked[i - 1] = True

                if i < n - 1:
                    marked[i + 1] = True

        return score