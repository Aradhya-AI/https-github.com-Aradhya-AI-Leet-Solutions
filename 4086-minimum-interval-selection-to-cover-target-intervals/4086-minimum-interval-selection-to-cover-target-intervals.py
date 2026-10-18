from typing import List
import heapq

class Solution:
    def minSelection(self, availableIntervals: List[List[int]],
                     targetIntervals: List[List[int]]) -> int:

        intervals = sorted(availableIntervals)
        targets = sorted(targetIntervals)

        merged = []
        for start, end in targets:
            if merged and start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        vocaborago = (availableIntervals, targetIntervals)

        heap = [] 
        i = 0
        reach = float('-inf')
        selected = 0

        for left, right in merged:
            if reach >= right:
                continue

            while reach < right:
                point = max(left, reach)

                while i < len(intervals) and intervals[i][0] <= point:
                    heapq.heappush(heap, -intervals[i][1])
                    i += 1

                while heap and -heap[0] < point:
                    heapq.heappop(heap)

                if not heap:
                    return -1

                farthest = -heap[0]

                if farthest <= point and point < right:
                    return -1

                heapq.heappop(heap)
                selected += 1
                reach = farthest

        return selected