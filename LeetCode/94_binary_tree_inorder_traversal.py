# Solved

# By 14.06.2024:
# Runtime = 41 ms (beats 15.50% of users)
# Memory = 16.42 MB (beats 65.74% of users)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Create an empty result list
        stack = []
        
        # Check if "root" is empty
        if root is None or root.val is None:
            return stack
        
        # Check if "root" contains a left subtree
        if root.left is not None:
            # Make the subtree as a "root", work with him and 
            # insert all the got values
            stack.extend(self.inorderTraversal(root.left))
        
        # Insert curren value of "root"
        stack.append(root.val)
        
        # Check if "root" contains a right subtree
        if root.right is not None:
            # Make the subtree as a "root", work with him and 
            # insert all the got values
            stack.extend(self.inorderTraversal(root.right))
            
        # Return the result list
        return stack
        
        
if __name__ == '__main__':
    root = TreeNode(1, TreeNode(None), TreeNode(2, TreeNode(3)))
    print(Solution().inorderTraversal(root))
    
    root = None
    print(Solution().inorderTraversal(root))
    
    root = TreeNode(1)
    print(Solution().inorderTraversal(root))