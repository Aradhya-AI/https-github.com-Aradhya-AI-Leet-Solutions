class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = {}
        operations = 0

        for num in nums:
            complement = k - num

            if counts.get(complement, 0) > 0:
                counts[complement] -= 1
                operations += 1
            else:
                counts[num] = counts.get(num, 0) + 1

        return operations
