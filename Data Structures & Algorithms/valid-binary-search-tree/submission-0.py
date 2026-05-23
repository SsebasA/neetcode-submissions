# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, max_val, min_val):
            if not node:
                return True
            
            if not (min_val < node.val < max_val):
                return False
            
            return (validate(node.left, node.val, min_val) and validate(node.right, max_val, node.val))
        
        ans = validate(root, float("inf"), float("-inf"))
    
        return ans

