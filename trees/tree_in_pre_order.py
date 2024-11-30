# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_ix = {value:ix for ix, value in enumerate(inorder)}

        def build_subtree(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            value = preorder[pre_left]
            node = TreeNode(value)
            root_in_ix = inorder_ix[value]

            size_left_st = root_in_ix - in_left
            size_right_st = in_right - root_in_ix

            node.left = build_subtree(pre_left + 1, pre_left + size_left_st, in_left, root_in_ix - 1 )
            node.right = build_subtree(pre_right - size_right_st + 1, pre_right, root_in_ix + 1, in_right )

            return node
        
        return build_subtree(0, len(preorder) - 1, 0, len(preorder) - 1)