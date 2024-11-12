from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize a counter and result variable
        self.count = 0
        self.result = None

        # Helper function for in-order traversal
        def inorder_traversal(node):
            if node is None or self.result is not None:
                return
            
            # Traverse the left subtree
            inorder_traversal(node.left)
            
            # Visit the current node
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            
            # Traverse the right subtree
            inorder_traversal(node.right)
        
        # Perform in-order traversal
        inorder_traversal(root)
        return self.result
