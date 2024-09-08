# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ## Visit left and right
        def visitNodes(node, level, level_lists):
            if node is None:
                return level - 1
            
            if level in level_lists:
                level_lists[level].append(node.val)
            else:
                level_lists[level] = [node.val]
            
            left_level = visitNodes(node.left, level+1, level_lists)
            right_level = visitNodes(node.right, level+1, level_lists)
            
            return max(right_level, left_level)

        level_lists = {}
        if not root:
            return []
        
        max_level = visitNodes(root, 0, level_lists)
        print(level_lists[0])
        level_averages = []
        avg_size = 1
        for i in range(max_level+1):
            if i > 0:
                avg_size = len(level_lists[i])
            level_averages.append(sum(level_lists[i])/avg_size)

        return level_averages

