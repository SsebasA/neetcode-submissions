from _heapq import heapify, heappop, heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        freq = list(counts.values())

        max_freq = max(freq)
        max_freq_count = freq.count(max_freq)

        ans = (max_freq - 1) * (n + 1) + max_freq_count

        return max(ans, len(tasks))

