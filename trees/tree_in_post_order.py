# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_ix = {value:ix for ix, value in enumerate(inorder)}

        def build_subtree(post_left, post_right, in_left, in_right):
            if post_left > post_right:
                return None

            value = postorder[post_right]
            node = TreeNode(value)
            root_in_ix = inorder_ix[value]

            size_right_st = in_right - root_in_ix

            node.left = build_subtree(post_left, post_right - size_right_st - 1, in_left, root_in_ix - 1 )      
            node.right = build_subtree(post_right - size_right_st, post_right - 1, root_in_ix + 1, in_right )

            return node
        
        return build_subtree(0, len(inorder) - 1, 0, len(inorder) - 1)