from heapq import heappop, heapify, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.h = []

        heapify(self.h)
        for num in nums:
            self.add(num)
        


    def add(self, val: int) -> int:
        heappush(self.h, val)
        if len(self.h) > self.k:
            heappop(self.h)
        
        return self.h[0]




        
