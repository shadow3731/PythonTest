# Solved

# By 16.06.2024:
# Runtime = 43 ms (beats 35.51% of users)
# Memory = 17.51 MB (beats 74.93% of users)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
            
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 0 if root == None else 1 + max(
            self.maxDepth(root.left), self.maxDepth(root.right)
        )
        

if __name__ == '__main__':
    root = TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7)),
    )
    print(Solution().maxDepth(root))
    
    root = TreeNode(1, None, TreeNode(2))
    print(Solution().maxDepth(root))