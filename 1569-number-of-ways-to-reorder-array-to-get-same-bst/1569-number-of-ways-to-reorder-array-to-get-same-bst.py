
from math import comb
import sys

sys.setrecursionlimit(10000)

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def countWays(arr):

            if len(arr) <= 2:
                return 1

            root = arr[0]

            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            positions = comb(len(arr) - 1, len(left))

            leftWays = countWays(left)
            rightWays = countWays(right)

            return (
                positions * leftWays * rightWays
            ) % MOD
            
        return (countWays(nums) - 1) % MOD
