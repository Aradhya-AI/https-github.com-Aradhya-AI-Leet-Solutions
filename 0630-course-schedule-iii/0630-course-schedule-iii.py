class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        import heapq

        courses.sort(key=lambda x: x[1])
        max_heap = []
        total_time = 0

        for duration, deadline in courses:
            total_time += duration
            heapq.heappush(max_heap, -duration)

            if total_time > deadline:
                total_time += heapq.heappop(max_heap)

        return len(max_heap)