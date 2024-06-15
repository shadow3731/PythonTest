# Solved

# By 15.06.2024:
# Runtime = 43 ms (beats 15.63% of users)
# Memory = 16.75 MB (beats 12.75% of users)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Check if "root" is empty
        if root is None or root.val is None:
            return True
        
        # Check if 1 of subtrees is empty
        if (
            (root.left is None and root.right is not None) 
            or (root.left is not None and root.right is None)
        ):
            return False
        
        # Get left and right branches of "root"
        p: TreeNode = root.left
        q: TreeNode = root.right
        
        # Define the function which will return TreeNode objects 
        # as a list of their values. Reversed parameter means 
        # that we need to make a list starting from the right 
        # lower node, not from the left lower one 
        def inorderTraversal(root: TreeNode, reversed: bool=False) -> List[int]:
            # Create an empty result list
            stack = []
            
            # Check if "root" is empty
            if root is None or root.val is None:
                return stack
            
            # Check if need to go reversed
            if reversed is True:
                # Check if "root" contains a left subtree
                if root.left is not None:
                    # Make the subtree as a "root", work with him and 
                    # insert all the got values
                    stack.append(inorderTraversal(root.left, True))
                    
            else:
                # Check if "root" contains a right subtree
                if root.right is not None:
                    # Make the subtree as a "root", work with him and 
                    # insert all the got values
                    stack.append(inorderTraversal(root.right))
            
            # Insert curren value of "root"
            stack.append(root.val)
            
            # Check if need to go reversed
            if reversed is True:
                # Check if "root" contains a right subtree
                if root.right is not None:
                    # Make the subtree as a "root", work with him and 
                    # insert all the got values
                    stack.append(inorderTraversal(root.right, True))
                    
            else:
                # Check if "root" contains a left subtree
                if root.left is not None:
                    # Make the subtree as a "root", work with him and 
                    # insert all the got values
                    stack.append(inorderTraversal(root.left))
                
            # Return the result list
            return stack
        
        # Get a list of the left branch of "root"
        p_list = inorderTraversal(p)
        # Get a list of the right branch of "root", but reversed
        q_list = inorderTraversal(q, True)
        
        # Return comparison of 2 lists
        return p_list == q_list
    
    
if __name__ == '__main__':
    root = TreeNode(
        1, 
        TreeNode(2, TreeNode(3), TreeNode(4)), 
        TreeNode(2, TreeNode(4), TreeNode(3)),
    )
    print(Solution().isSymmetric(root))
    
    root = TreeNode(
        2,
        TreeNode(3, TreeNode(4), TreeNode(
            5, TreeNode(8), TreeNode(9)
            )),
        TreeNode(3, TreeNode(
            5, TreeNode(9), TreeNode(8)
            ), TreeNode(4)),
    )
    print(Solution().isSymmetric(root))