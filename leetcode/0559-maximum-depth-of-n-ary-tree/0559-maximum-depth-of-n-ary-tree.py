"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth=0
        q=deque([root])

        while q:
            depth+=1
            n=len(q)
            for _ in range(n):
                node=q.popleft()
                
                for child in node.children:
                    if child:
                        q.append(child)
        
        return depth
