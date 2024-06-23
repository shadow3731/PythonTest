# Solved

# By 23.06.2024:
# Runtime = 41 ms (beats 55.72% of users)
# Memory = 17.28 MB (beats 95.31% of users)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Check if "root" is empty
        if root is None or root.val is None:
            return False
        
        # Check if "root" is a leaf
        if root.left is None and root.right is None:
            # Check if root-leaf equals to target sum
            return True if root.val == targetSum else False
        
        # A function to find if there's a sum path
        def inner(root: TreeNode, target_sum: int, curr_sum: int) -> bool:
            # Check if a node is empty
            if root is None or root.val is None:
                return False
            
            # Check if a node is a leaf
            if root.left is None and root.right is None:
                # Check if the sum of a node value and the sum of 
                # the previous path equals to the target sum
                return root.val + curr_sum == target_sum
            
            # Variables to show if there's a sum path
            left_result, right_result = False, False
            # The sum from the root until the current node
            curr_sum += root.val
            
            # Check if the node contains the left subtree        
            if root.left is not None:
                # Go deeper to the left subtree
                left_result = inner(
                    root.left, 
                    target_sum, 
                    curr_sum
                )
            
            # Check if a path along the left subtree is not a path 
            # sum and if the node contains the right subtree    
            if left_result is False and root.right is not None:
                # Go deeper to the right subtree
                right_result = inner(
                    root.right, 
                    target_sum, 
                    curr_sum
                )
            
            # Check if any path is a path sum        
            return left_result is True or right_result is True
        
        # Check if any path is a path sum    
        return (
            inner(root.left, targetSum, root.val)
            or inner(root.right, targetSum, root.val)
        )
                
if __name__ == '__main__':
    root = TreeNode(
        5,
        TreeNode(
            4,
            TreeNode(11, TreeNode(7), TreeNode(2))
        ),
        TreeNode(
            8,
            TreeNode(13),
            TreeNode(4, None, TreeNode(1))
        )
    )
    targetSum = 22
    print(Solution().hasPathSum(root, targetSum))
    
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    targetSum = 5
    print(Solution().hasPathSum(root, targetSum))
    
    root = None
    targetSum = 0
    print(Solution().hasPathSum(root, targetSum))
    
    root = TreeNode(1)
    targetSum = 1
    print(Solution().hasPathSum(root, targetSum))
    
    root = TreeNode(-2, None, TreeNode(-3))
    targetSum = -5
    print(Solution().hasPathSum(root, targetSum))