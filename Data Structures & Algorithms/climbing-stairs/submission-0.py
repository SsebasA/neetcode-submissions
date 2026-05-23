class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0] * (n + 1)

        def climb(n, cache):
            if n <= 2:
                return n 
            
            if cache[n] != 0:
                return cache[n]
            else:
                cache[n] = climb(n - 1, cache) + climb(n - 2, cache)
                return cache[n]
        
        return climb(n, cache)