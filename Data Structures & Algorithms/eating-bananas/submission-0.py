class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        k_ans = high

        def calc_hrs(k):
            hours = 0
            for p in piles:
                hrs = math.ceil(p / k)
                hours += hrs

            return hours

        while low <= high:
            mid = low + (high - low) // 2
            if calc_hrs(mid) <= h:
                k_ans = min(k_ans, mid)
                high = mid - 1
            elif calc_hrs(mid) > h:
                low = mid + 1
        
        return k_ans
            
        