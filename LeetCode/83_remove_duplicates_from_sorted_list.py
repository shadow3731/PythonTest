# Solved

# By 12.06.2024:
# Runtime = 37 ms (beats 76.54% of users)
# Memory = 16.35 MB (beats 99.12% of users)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
            
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # Check if "head" is empty
        if head is None or head.val is None:
            return None
        
        # Create another object linked with "head" object
        result = head
        
        # Start an endless cycle
        while True:
            # Check if there's no next element
            if head.next is None:
                # Return whole ListNode with no dublicates
                return result
            
            # Check if current value equals to the next one
            if head.val == head.next.val:
                # Go to the next value inside of the next object
                head.next = head.next.next
            else:
                # Capture next object and work with him
                head = head.next
            
if __name__ == '__main__':
    head = ListNode(1, ListNode(1, ListNode(2)))
    print(Solution().deleteDuplicates(head))
    
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    print(Solution().deleteDuplicates(head))
    
    head = None
    print(Solution().deleteDuplicates(head))