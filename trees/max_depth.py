# Definition for a binary tree node. https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution:         
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            if root.val == None:
                return 0
            else:
                return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0