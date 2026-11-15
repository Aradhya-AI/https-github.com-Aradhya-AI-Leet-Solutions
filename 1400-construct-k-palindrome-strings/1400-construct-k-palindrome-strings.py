class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        odd_count = 0
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for count in freq.values():
            if count % 2 == 1:
                odd_count += 1

        return odd_count <= k