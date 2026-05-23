class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            days = 0
            while stack and temperatures[i] > temperatures[stack[-1]]:
                old_idx = stack.pop()
                days = i - old_idx
                res[old_idx] = days
            
            stack.append(i)
        

        return res
            