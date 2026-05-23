# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                actual_node = queue.popleft()

                if i == level_size - 1:
                    res.append(actual_node.val)
                
                if actual_node.left:
                    queue.append(actual_node.left)
                
                if actual_node.right:
                    queue.append(actual_node.right)
        

        return res