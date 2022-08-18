import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapify(heap)
        for i in stones:
            heapq.heappush(heap, i * -1)
            
        while len(heap) > 1:
            print(heap)
            x = heapq.heappop(heap) * -1
            y = heapq.heappop(heap) * -1
            if x != y:
                heapq.heappush(heap, (x - y) * -1)
        if len(heap) == 1:
            return heapq.heappop(heap) * -1
        return 0
