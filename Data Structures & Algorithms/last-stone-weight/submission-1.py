from heapq import heappop, heapify, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapify(heap)

        for stone in stones:
            heappush(heap, -stone)

        
        while len(heap) >= 2:
            elem_x = heappop(heap)
            elem_y = heappop(heap)
            print("Elements after pop: ", [-i for i in heap])
            if elem_x < elem_y:
                new_w = elem_y - elem_x
                heappush(heap, -new_w)
            elif elem_x == elem_y:
                heappush(heap, 0)

        return -heap[0]


        