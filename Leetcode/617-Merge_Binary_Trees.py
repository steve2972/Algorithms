from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            val = TreeNode(root1.val + root2.val)
            val.left = self.mergeTrees(root1.left, root2.left)
            val.right = self.mergeTrees(root1.right, root2.right)
            return val
        else:
            return root1 if root1 else root2

