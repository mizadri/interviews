class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth, right_view):
            if not node:
                return
            
            # If this is the first time we've visited this depth, add the node's value
            if depth == len(right_view):
                right_view.append(node.val)
            
            # Visit the right child first, then the left child
            dfs(node.right, depth + 1, right_view)
            dfs(node.left, depth + 1, right_view)
        
        right_view = []
        dfs(root, 0, right_view)
        return right_view
