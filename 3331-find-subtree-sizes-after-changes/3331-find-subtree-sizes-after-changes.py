class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}

        def dfs(u):
            ch = s[u]
            old = last.get(ch, -1)

            if old != -1:
                new_parent[u] = old

            last[ch] = u

            for v in children[u]:
                dfs(v)

            if old == -1:
                last.pop(ch, None)
            else:
                last[ch] = old

        dfs(0)

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [1] * n

        def count(u):
            for v in new_children[u]:
                ans[u] += count(v)
            return ans[u]

        count(0)
        return ans