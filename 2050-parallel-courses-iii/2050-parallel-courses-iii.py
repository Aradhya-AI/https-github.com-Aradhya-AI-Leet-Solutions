class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        from collections import deque

        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for prev, nxt in relations:
            graph[prev - 1].append(nxt - 1)
            indegree[nxt - 1] += 1

        q = deque()
        dp = time[:]

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()

            for v in graph[u]:
                dp[v] = max(dp[v], dp[u] + time[v])
                indegree[v] -= 1

                if indegree[v] == 0:
                    q.append(v)

        return max(dp)