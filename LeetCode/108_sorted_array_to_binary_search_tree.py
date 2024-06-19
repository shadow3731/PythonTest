# Solved

# By 19.06.2024:
# Runtime = 51 ms (beats 76.89% of users)
# Memory = 17.79 MB (beats 71.43% of users)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Check if list is empty
        if nums is None or len(nums) == 0:
            return None
        
        # Get the middle index of the list
        middle_index = len(nums) // 2
        # Get the value at the middle index of the list 
        # and store it as a node value
        treenode = TreeNode(nums[middle_index])
        
        # Check if the list contains other values
        if len(nums) > 1:
            # Get and store the value for both left and right 
            # subtrees. For the left subtree we get all values 
            # from the list going until the middle value. For 
            # the right subtree we get all values from the list 
            # going after the middle value
            treenode.left = self.sortedArrayToBST(nums[:middle_index])
            treenode.right = self.sortedArrayToBST(nums[middle_index+1:])
        
        # Return binary search tree or a subtree
        return treenode
            
        
if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    Solution().sortedArrayToBST(nums)