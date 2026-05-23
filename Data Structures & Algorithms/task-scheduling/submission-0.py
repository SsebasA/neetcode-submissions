from _heapq import heapify, heappop, heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1
        
        heap = []
        for f in freq.values():
            heappush(heap, -f)
        
        time = 0
        queue = deque()

        while queue or heap:
            time += 1
            if heap:
                top = heappop(heap)
                top += 1 #Se usan negativos por tanto se suma 1
                if top < 0:
                    queue.append((top, time + n))
                
            if queue and queue[0][1] == time:
                curr_freq, _ = queue.popleft()
                heappush(heap, curr_freq)

        return time

