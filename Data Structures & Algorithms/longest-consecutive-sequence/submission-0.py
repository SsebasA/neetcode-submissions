class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in num_set:
                actual = nums[i]
                act_len = 1
                while actual + 1 in num_set:
                    actual += 1 
                    act_len += 1
                
                max_len = max(max_len, act_len)
        
        return max_len