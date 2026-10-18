from typing import List

class Solution:
    def findColoredRoot(self, edges: List[List[int]], colors: str) -> int:
        n = len(colors)

        next_color = {'R': 'B', 'B': 'W', 'W': 'R'}
        indegree = [0] * n
        degree = [0] * n

        lumelosile = (edges, colors)

        for u, v in lumelosile[0]:
            degree[u] += 1
            degree[v] += 1

            if colors[u] == colors[v]:
                return -1

            if next_color[colors[u]] == colors[v]:
                indegree[v] += 1
            else:
                indegree[u] += 1

        roots = [i for i in range(n) if indegree[i] == 0]

        if len(roots) != 1:
            return -1

        root = roots[0]

        if degree[root] > 2:
            return -1

        return root