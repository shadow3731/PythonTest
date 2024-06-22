# Solved

# By 22.06.2024:
# Runtime = 258 ms (beats 50.73% of users)
# Memory = 43.17 MB (beats 70.10% of users)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Check if "root" is empty
        if root is None or root.val is None:
            return 0
        
        # A function to define minimum depth of the left and right 
        # subtrees
        def get_min_depth(root: TreeNode) -> int:
            # Check if "root" is empty or its subtrees are empty
            if (
                root is None or root.val is None or 
                (root.left is None and root.right is None)
            ):
                return 1
            
            # Check if both subtrees are not empty
            if root.left is not None and root.right is not None:
                # Increase depth value
                left_depth, right_depth = 1, 1
                
                # Go deeper along the tree
                left_depth = get_min_depth(root.left) + 1
                right_depth = get_min_depth(root.right) + 1
                
                # Return the less value
                return min(left_depth, right_depth)
            
            else:
                # Check if the left subtree is not empty
                if root.left is not None:
                    # Go deeper along the left subtree
                    return get_min_depth(root.left) + 1
                
                else:
                    # Go deeper along the right subtree
                    return get_min_depth(root.right) + 1
        
        # Check if both subtrees are not empty
        if root.left is not None and root.right is not None:
            # Define the depth of the left and right subtrees
            left_depth = get_min_depth(root.left) + 1
            right_depth = get_min_depth(root.right) + 1
            
            # Return the less value
            return min(left_depth, right_depth)
        
        # Check if only the left tree is not empty
        elif root.left is not None and root.right is None:
            # Define the depth of the left subtree
            return get_min_depth(root.left) + 1
        
        # Check if only the right tree is not empty
        elif root.left is None and root.right is not None:
            # Define the depth of the right subtree
            return get_min_depth(root.right) + 1
        
        else:
            # Return 1, because root value is the 1st depth level
            return 1
            
if __name__ == '__main__':
    root = TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7))
    )
    print(Solution().minDepth(root))
    
    root = TreeNode(
        3, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))
    )
    print(Solution().minDepth(root))
    
    root = None
    print(Solution().minDepth(root))
    
    root = TreeNode(0)
    print(Solution().minDepth(root))