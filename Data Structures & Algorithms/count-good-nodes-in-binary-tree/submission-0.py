# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.DFS(root, root.val)
        
    
    def DFS(self, node, max_so_far):
        if not node:
            return 0
        
        curr_good = 1 if node.val >= max_so_far else 0

        new_max = max(node.val, max_so_far)

        return curr_good + self.DFS(node.left, new_max) + self.DFS(node.right, new_max)
    




        