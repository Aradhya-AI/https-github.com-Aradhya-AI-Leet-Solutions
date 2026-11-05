class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        from collections import deque

        q = deque([(s1, 0)])
        visited = {s1}
        n = len(s1)

        while q:
            s, steps = q.popleft()

            if s == s2:
                return steps

            i = 0
            while s[i] == s2[i]:
                i += 1

            for j in range(i + 1, n):
                if s[j] == s2[i] and s[j] != s2[j]:
                    arr = list(s)
                    arr[i], arr[j] = arr[j], arr[i]
                    nxt = ''.join(arr)

                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))

                    if s[j] == s2[j]:
                        break