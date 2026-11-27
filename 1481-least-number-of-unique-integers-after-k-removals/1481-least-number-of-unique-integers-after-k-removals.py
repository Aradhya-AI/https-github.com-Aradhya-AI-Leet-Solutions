class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        from collections import Counter

        freq = sorted(Counter(arr).values())
        ans = len(freq)

        for count in freq:
            if k >= count:
                k -= count
                ans -= 1
            else:
                break

        return ans