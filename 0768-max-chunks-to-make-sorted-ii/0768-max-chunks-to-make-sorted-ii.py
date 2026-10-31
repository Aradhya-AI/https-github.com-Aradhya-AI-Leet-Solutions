class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        suffix_min = [0] * n

        suffix_min[-1] = arr[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(arr[i], suffix_min[i + 1])

        chunks = 1
        max_value = arr[0]

        for i in range(n - 1):
            max_value = max(max_value, arr[i])

            if max_value <= suffix_min[i + 1]:
                chunks += 1

        return chunks
