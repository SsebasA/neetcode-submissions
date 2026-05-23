# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        
        cola = deque([root])
        while cola:
            list_nivel = []
            nivel_actual = len(cola)
            for _ in range(nivel_actual):
                nodo_actual = cola.popleft()
                list_nivel.append(nodo_actual.val)
                if nodo_actual.left:
                    cola.append(nodo_actual.left)
                if nodo_actual.right:
                    cola.append(nodo_actual.right)
            
            res.append(list_nivel)
        
        return res
        