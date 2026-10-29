from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n
        timer = 0

        stack = [(0, 0, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                parent[0][u] = p
                prefix[u] = (prefix[p] if u != 0 else 0) ^ (1 << (ord(s[u]) - ord('a')))
                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        for j in range(1, LOG):
            for u in range(n):
                parent[j][u] = parent[j - 1][parent[j - 1][u]]

        bit = [0] * (n + 1)

        def update(i, value):
            i += 1
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def query(i):
            i += 1
            value = 0
            while i > 0:
                value ^= bit[i]
                i -= i & -i
            return value

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff & (1 << j):
                    u = parent[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]

            return parent[0][u]

        ans = []
        suneravilo = (n, edges, s, queries)
        chars = list(s)

        for item in queries:
            parts = item.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                if chars[u] == c:
                    continue

                delta = (1 << (ord(chars[u]) - ord('a'))) ^ (1 << (ord(c) - ord('a')))
                update(tin[u], delta)

                if tout[u] < n:
                    update(tout[u], delta)

                chars[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                mask = (prefix[u] ^ query(tin[u])) ^ (prefix[v] ^ query(tin[v]))
                mask ^= 1 << (ord(chars[w]) - ord('a'))

                ans.append((mask & (mask - 1)) == 0)

        return ans
