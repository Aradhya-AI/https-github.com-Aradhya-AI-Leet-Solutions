import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.heap = []
        self.added = set()

    def popSmallest(self) -> int:
        if self.heap:
            num = heapq.heappop(self.heap)
            self.added.remove(num)
            return num

        num = self.current
        self.current += 1
        return num

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)
