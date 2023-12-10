class MedianFinder:

    def __init__(self):
        self.small_half = []
        self.large_half = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_half, num)
        largest_of_small = heapq.heappop(self.small_half)
        heapq.heappush(self.large_half, - largest_of_small)
        if len(self.large_half) > len(self.small_half):
            smallest_of_large = -heapq.heappop(self.large_half)
            heapq.heappush(self.small_half, smallest_of_large)
            


    def findMedian(self) -> float:
        if len(self.small_half) == len(self.large_half):
            return (self.small_half[0] - self.large_half[0]) / 2.0
        else:
            return float(self.small_half[0])
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()