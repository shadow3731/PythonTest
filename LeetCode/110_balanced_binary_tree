# Solved

# By 21.06.2024:
# Runtime = 326 ms (beats 5.23% of users)
# Memory = 18.18 MB (beats 12.56% of users)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Check if "root" is None or both of its subtrees 
        # are None
        if (
            root is None
            or (root.left is None and root.right is None)
        ):
            return True
        
        # Function for defining the depth of a node
        def define_max_depth(root: Optional[TreeNode]) -> int:
            # Check if node is None
            if root is None:
                return 0
            
            # Get initial depth value to both sides as 1
            left_depth, right_depth = 1, 1
            
            # Check if left subtree is not empty
            if root.left is not None:
                # Go next to the subtree increasing the depth
                left_depth += define_max_depth(root.left)
            
            # Check if right subtree is not empty
            if root.right is not None:
                # Go next to the subtree increasing the depth
                right_depth += define_max_depth(root.right)
            
            # Check if left subtree is deeper than the right one    
            if left_depth > right_depth:
                # Get the left depth
                return left_depth
            else:
                # Get the right depth
                return right_depth
        
        # A list of all nodes in the certain depth
        subtree_curr_gen: list[TreeNode] = [root]
        # A list of all nodes in the 1 level deeper
        subtree_next_gen: list[TreeNode] = []
        
        from copy import deepcopy
        
        # Start an endless cycle    
        while True:
            # Check every subtree in the certain depth
            for subtree in subtree_curr_gen:
                # Get the subtree depth of the left and right 
                # sides
                left_depth = define_max_depth(subtree.left)
                right_depth = define_max_depth(subtree.right)

                # Check if the left and right depths deffer more 
                # than 1 level
                if abs(right_depth - left_depth) > 1:
                    # The treenode object is not high-balanced
                    return False
                
                else:
                    # Check if the left subtree is not empty       
                    if subtree.left is not None:
                        # Store the node which is 1 level deeper
                        subtree_next_gen.append(subtree.left)
                    
                    # Check if the right subtree is not empty    
                    if subtree.right is not None:
                        # Store the node which is 1 level deeper
                        subtree_next_gen.append(subtree.right)
            
            # Check if there's any nodes deeper than the current
            # ones            
            if len(subtree_next_gen) > 0:
                # Store and use new nodes
                subtree_curr_gen = deepcopy(subtree_next_gen)
                # Clear the list of new nodes
                subtree_next_gen.clear()
            
            else:
                break
        
        # The treenode object is high-balanced
        return True
        
        
if __name__ == '__main__':
    root = TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7))
    )
    print(Solution().isBalanced(root))
    
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
        TreeNode(2)
    )
    print(Solution().isBalanced(root))
    
    root = TreeNode(
        1,
        None,
        TreeNode(2, None, TreeNode(3))
    )
    print(Solution().isBalanced(root))
    
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(3, TreeNode(4))),
        TreeNode(2, None, TreeNode(3, None, TreeNode(4)))
    )
    print(Solution().isBalanced(root))