# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_index = 0  # Track current position in preorder
        
        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            # Base case: invalid range means no subtree exists
            if left > right:
                return None
            
            # Get current root value from preorder and advance index
            root_val = preorder[self.pre_index]
            self.pre_index += 1
            
            # Create root node
            root = TreeNode(root_val)
            
            # Find position of root in inorder array
            index = inorder_map[root_val]
            
            # Build left and right subtrees recursively
            # Left subtree uses elements from left to index-1
            root.left = array_to_tree(left, index - 1)
            # Right subtree uses elements from index+1 to right
            root.right = array_to_tree(index + 1, right)
            
            return root
        
        return array_to_tree(0, len(inorder) - 1)   