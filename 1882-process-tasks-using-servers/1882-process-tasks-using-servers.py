class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        import heapq

        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        result = []
        time = 0

        for i, task in enumerate(tasks):
            time = max(time, i)

            if not available and busy[0][0] > time:
                time = busy[0][0]

            while busy and busy[0][0] <= time:
                _, weight, server = heapq.heappop(busy)
                heapq.heappush(available, (weight, server))

            weight, server = heapq.heappop(available)
            result.append(server)

            heapq.heappush(busy, (time + task, weight, server))

        return result