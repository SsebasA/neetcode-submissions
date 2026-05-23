# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_diameter = 0

        def DFS(root):
            if not root:
                return 0
            
            alt_izq = DFS(root.left)
            alt_der = DFS(root.right)

            nonlocal max_diameter
            max_diameter = max(max_diameter, alt_der+alt_izq)

            return 1 + max(alt_izq, alt_der)

        DFS(root)

        return max_diameter
            
        




            