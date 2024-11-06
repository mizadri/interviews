

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def rightify(node):
            if node is None:
                return None
            
            # Get flattened lists for left and right subtrees
            left_tail = rightify(node.left)
            right_tail = rightify(node.right)
            
            # Save the right subtree for reattaching after flattening the left subtree
            original_right = node.right
            
            # Flatten the left subtree into the right of the current node
            if node.left:
                node.right = node.left
                node.left = None
                left_tail.right = original_right
            
            # Return the tail of the current flattened tree
            return right_tail if right_tail else left_tail if left_tail else node

        rightify(root)
