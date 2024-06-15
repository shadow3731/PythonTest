# Solved

# By 15.06.2024:
# Runtime = 32 ms (beats 75.67% of users)
# Memory = 16.59 MB (beats 44.83% of users)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if both TreeNodes are empty
        if p is None and q is None:
            return True
        
        # Check if 1 of 2 TreeNodes is empty
        if (
            (p is None and q is not None) 
            or (p is not None and q is None)
        ):
            return False
        
        # Define the function which will return TreeNode objects 
        # as a list of their values
        def inorderTraversal(root: TreeNode) -> List[int]:
            # Create an empty result list
            stack = []
            
            # Check if "root" is empty
            if root is None or root.val is None:
                return stack
            
            # Check if "root" contains a left subtree
            if root.left is not None:
                # Make the subtree as a "root", work with him and 
                # insert all the got values
                stack.append(inorderTraversal(root.left))
            
            # Insert curren value of "root"
            stack.append(root.val)
            
            # Check if "root" contains a right subtree
            if root.right is not None:
                # Make the subtree as a "root", work with him and 
                # insert all the got values
                stack.append(inorderTraversal(root.right))
                
            # Return the result list
            return stack
        
        # Return comparison of 2 lists
        return inorderTraversal(p) == inorderTraversal(q)
    
    
if __name__ == '__main__':
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    Solution().isSameTree(p, q)
    
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    Solution().isSameTree(p, q)