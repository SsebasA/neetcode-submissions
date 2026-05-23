# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth = 0
        cola: deque[TreeNode] = deque([root])
        while cola:
            nodos_en_nivel = len(cola)
            for _ in range(nodos_en_nivel):
                nodo_actual = cola.popleft()
                if nodo_actual.left:
                    cola.append(nodo_actual.left)
                if nodo_actual.right:
                    cola.append(nodo_actual.right)

            depth += 1
    
        return depth



        

        