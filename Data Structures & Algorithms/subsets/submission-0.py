class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sack = []

        def backtrack(idx):
            if idx == len(nums):
                res.append(sack[:])
                return
            
            sack.append(nums[idx])
            backtrack(idx + 1)
            sack.pop()
            backtrack(idx + 1)
        
        idx = 0
        backtrack(idx)
        
        return res
