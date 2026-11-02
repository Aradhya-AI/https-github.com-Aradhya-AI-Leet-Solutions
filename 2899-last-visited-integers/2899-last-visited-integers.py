class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        result = []
        k = 0

        for num in nums:
            if num == -1:
                k += 1
                if k <= len(seen):
                    result.append(seen[-k])
                else:
                    result.append(-1)
            else:
                seen.append(num)
                k = 0

        return result
