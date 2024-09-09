class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val == q.val:
                if p.left == None and q.left == None and p.right == None and q.right == None:
                    return True
                else:
                    return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            else:
                return False
        else:
            if p == q:
                return True
            else:
                return False