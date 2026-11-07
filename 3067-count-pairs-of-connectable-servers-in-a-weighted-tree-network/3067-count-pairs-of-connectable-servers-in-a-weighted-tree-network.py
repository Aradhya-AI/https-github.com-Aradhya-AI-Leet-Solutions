class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        from collections import defaultdict

        n = len(edges) + 1
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        ans = [0] * n

        def dfs(node, parent, dist):
            count = 1 if dist % signalSpeed == 0 else 0

            for nxt, weight in graph[node]:
                if nxt != parent:
                    count += dfs(nxt, node, dist + weight)

            return count

        for i in range(n):
            total = 0

            for neighbor, weight in graph[i]:
                count = dfs(neighbor, i, weight)
                ans[i] += total * count
                total += count

        return ans