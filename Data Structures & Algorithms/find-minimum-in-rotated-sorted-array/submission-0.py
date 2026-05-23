class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_elem = max(nums)

        for num in nums:
            min_elem = min(num, min_elem)
        
        return min_elem