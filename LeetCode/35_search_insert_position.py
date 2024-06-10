# Solved, but still wasn't tested on the condition about 
# O(log n) runtime compexity

# By 10.06.2024:
# Runtime = 46 ms (beats 78.26% of users)
# Memory = 17.30 MB (beats 76.56% of users)
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Check if "nums" is empty or if "nums" contains values 
        # and "target" is less than the 1st "nums" value
        if len(nums) == 0 or (len(nums) > 0 and target < nums[0]):
            return 0
        # Check if "nums" contains values and "targer" is greater 
        # than the last "nums" values
        if len(nums) > 0 and target > nums[-1]:
            return len(nums)
        
        # Create a copy of "nums" which will be sliced to find 
        # a target index
        parts = nums
        # A variable to point to a target index
        position = 0
        
        # Start an endless cycle
        while True:
            # Get a middle index of the list
            middle_index = len(parts) // 2
            # Add middle index value to a target position value. 
            # Because of we decrease the length of the initial list 
            # every time, we need to adjust the position value
            position += middle_index
            
            # Check if the current list is empty or if "target" 
            # value equals to a value located in the middle index 
            # of the current list 
            if len(parts) == 0 or target == parts[middle_index]:
                # Return target position
                return position
            
            # Check if there's 1 value left in the current list
            if len(parts) == 1:
                # Check if "target" value is less than the only 
                # element
                if target < parts[0]:
                    # Return target position
                    return position
                else:
                    # Return target position
                    return position + 1
            else:
                # Check if "target" value is less than a value 
                # located in the middle index of the current list 
                if target < parts[middle_index]:
                    # Get a halved list from the left
                    parts = parts[:middle_index]
                    # Adjust position value
                    position -= len(parts)
                else:
                    # Get a halved list from the right exlucding 
                    # the middle value
                    parts = parts[middle_index+1:]
                    # Adjust position value
                    position += 1
        
        
if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    print(Solution().searchInsert(nums, target))
    
    nums = [1, 3, 5, 6]
    target = 2
    print(Solution().searchInsert(nums, target))
    
    nums = [1, 3, 5, 6]
    target = 7
    print(Solution().searchInsert(nums, target))
    
    nums = [1, 3, 5]
    target = 4
    print(Solution().searchInsert(nums, target))