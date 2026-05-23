# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        def level_order(p, q) -> bool:
            cola_p = deque([p])
            cola_q = deque([q])

            while cola_p and cola_q:
                if len(cola_p) > 0 and len(cola_q):
                    nodo_ac_p = cola_p.popleft()
                    nodo_ac_q = cola_q.popleft()

                    if not nodo_ac_p and not nodo_ac_q:
                        continue

                    if not nodo_ac_p or not nodo_ac_q:
                        return False

                    if nodo_ac_p.val == nodo_ac_q.val:
                        cola_p.append(nodo_ac_p.left)
                        cola_p.append(nodo_ac_p.right)
                        cola_q.append(nodo_ac_q.left)
                        cola_q.append(nodo_ac_q.right)
                    else:
                        return False
                else:
                    return False
            return True

        
        is_same = level_order(p,q)
        
        return is_same
            


