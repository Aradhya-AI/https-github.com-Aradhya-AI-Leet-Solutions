class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        from functools import cmp_to_key

        arr = [bin(x)[2:] for x in nums]

        def compare(a, b):
            if a + b > b + a:
                return -1
            return 1

        arr.sort(key=cmp_to_key(compare))

        return int("".join(arr), 2)