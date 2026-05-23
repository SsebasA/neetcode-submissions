from _heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        x1 = 0
        y1 = 0
        res = []

        for point in points:
            x2 = point[0]
            y2 = point[1]

            dist = math.sqrt((x1 - x2)**2 + (y1-y2)**2)
            elem = (dist, [x2, y2])
            heappush(min_heap, elem)

        while k > 0:
            coord = heappop(min_heap)
            res.append(coord[1])
            k -= 1
        
        return res 
