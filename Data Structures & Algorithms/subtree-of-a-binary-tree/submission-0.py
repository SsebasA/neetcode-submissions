# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        cadena_root = self.serialize(root)
        cadena_subroot = self.serialize(subRoot)

        if cadena_subroot in cadena_root:
            return True
        else:
            return False
        
    
    def serialize(self,root):
        serial = ""
        if not root:
            return serial.join("x")
        

        res_izq = self.serialize(root.left)
        res_der = self.serialize(root.right)

        return str(root.val) + res_izq + res_der




        