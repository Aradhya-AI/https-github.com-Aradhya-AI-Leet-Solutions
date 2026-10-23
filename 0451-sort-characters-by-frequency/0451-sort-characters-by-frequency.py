from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        result = sorted(freq, key=lambda ch: freq[ch], reverse=True)

        return "".join(ch * freq[ch] for ch in result)
