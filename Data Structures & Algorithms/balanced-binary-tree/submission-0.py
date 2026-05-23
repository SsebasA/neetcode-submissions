# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        is_valid = True

        def DFS(root):
            if not root:
                return 0
        
            alt_izq = DFS(root.left)
            alt_der = DFS(root.right)

            diff = abs(alt_der - alt_izq)
            if diff > 1:
                nonlocal is_valid
                is_valid = False
            
            return 1 + max(alt_izq, alt_der)

        DFS(root)
        
        return is_valid