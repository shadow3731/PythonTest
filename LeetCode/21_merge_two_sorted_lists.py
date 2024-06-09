# Solved, but it's an absurd task

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
  
class Solution:
    def mergeTwoLists(
        self, 
        list1: ListNode | None, 
        list2: ListNode | None
    ) -> ListNode | None:
        # Check if both lists are None
        if list1 is None and list2 is None:
            return None
        
        # 2 variables of 1 result list node object. 
        # The 1st variable will contain all the result 
        # list node object starting from a head element. 
        # The 2nd one will point to the current element 
        # of the result list node object, but still linked with it 
        sorted_list_node = sorting_list_node = ListNode()
        # 2 variables below are to point to current elements 
        # of their list node objects
        curr_val1: ListNode = list1
        curr_val2: ListNode = list2
        
        # Start an endless cycle
        while True:
            # If there is no current element in the 1st 
            # list node object...
            if curr_val1 is None or curr_val1.val is None:
                # If there is no current element in the 2st 
                # list node object...
                if curr_val2 is None or curr_val2.val is None:
                    # Break the cycle
                    break
                
                else:
                    # Go to the method
                    curr_val2, sorting_list_node = self.__capture(
                    sorting_list_node,
                    curr_val2, 
                    curr_val1
                )
            
            # If there is no current element in the 2st 
            # list node object...        
            elif curr_val2 is None or curr_val2.val is None:
                # Go to the method
                curr_val1, sorting_list_node = self.__capture(
                    sorting_list_node,
                    curr_val1, 
                    curr_val2
                )
                    
            # Compare what's the current element from both of 
            # 2 list node objects is bigger
            elif curr_val1.val > curr_val2.val:
                # Go to the method
                curr_val2, sorting_list_node = self.__capture(
                    sorting_list_node,
                    curr_val2, 
                    curr_val1
                )
                
            else:
                # Go to the method
                curr_val1, sorting_list_node = self.__capture(
                    sorting_list_node,
                    curr_val1, 
                    curr_val2
                )
        
        return sorted_list_node
    
    def __capture(
        self, 
        result_list: ListNode,
        curr_val: ListNode, 
        other_val: ListNode
    ) -> ListNode:
        # Get a bigger element from 1 of 2 list node objects 
        # and put this value to the result list node object 
        # as the current element
        result_list.val = curr_val.val
        # Get the next element of this list node object
        curr_val = curr_val.next
        
        # If any list node object still contains elements...
        if curr_val is not None or other_val is not None:
            # Create a point to the next element in the 
            # result list node object
            result_list.next = ListNode()
            # Move to this point saving link with the whole 
            # result list node object
            result_list = result_list.next
        
        return curr_val, result_list
        
        
if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    Solution().mergeTwoLists(l1, l2)
    
    l1 = None
    l2 = None
    Solution().mergeTwoLists(l1, l2)