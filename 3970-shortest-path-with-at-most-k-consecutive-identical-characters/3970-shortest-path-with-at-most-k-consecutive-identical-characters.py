import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0

        pq = [(0, 0, 1)]

        while pq:
            cost, u, count = heapq.heappop(pq)

            if cost > dist[u][count]:
                continue

            if u == n - 1:
                return cost

            for v, w in adj[u]:
                next_count = count + 1 if labels[u] == labels[v] else 1

                if next_count > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][next_count]:
                    dist[v][next_count] = new_cost
                    heapq.heappush(pq, (new_cost, v, next_count))

        return -1
