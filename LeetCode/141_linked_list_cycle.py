# Solved. No results of this taks, because I didn't understand 
# the task itself and I copied the code
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Create another pointer
        fast = head
        
        # A cycle to go through every value until there's no 
        # null value
        while fast and fast.next:
            # The 1st pointer go 1 step next
            head = head.next
            # The 2nd pointer go 2 steps next
            fast = fast.next.next
            # Check if both pointers point to the same node
            if head is fast:
                return True
            
        return False
    
if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print(Solution().hasCycle(head))