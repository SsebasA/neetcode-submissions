class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        izq = [1] * n
        der = [1] * n

        for i in range(1, n):
            izq[i] = izq[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            der[i] = der[i + 1] * nums[i + 1]

        res = []
        for i in range(n):
            val = der[i] * izq[i]
            res.append(val)

        return res