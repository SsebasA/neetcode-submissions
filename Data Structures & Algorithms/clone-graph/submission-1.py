"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        hsmp = {}

        def clone(node):
            if not node:
                return None
            
            if node in hsmp:
                return hsmp[node]
            else:
                copy = Node(node.val)
                hsmp[node] = copy
                for neighbor in node.neighbors:
                    copy.neighbors.append(clone(neighbor))
                
                return copy
        
        return clone(node)

        
            



        

