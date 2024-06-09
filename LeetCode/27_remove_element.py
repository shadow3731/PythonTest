# Solved

# By 09.06.2024
# Runtime = 25 ms (beats 98.71% of users)
# Memory = 16.38 MB (beats 98.31% of users)
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Check if the list is empty
        if len(nums) == 0:
            return 0
        
        # A variable to point to values of the list from the start
        k = 0
        # A variable to point to values of the list from the end
        i = len(nums)
        
        # Start an endless cycle
        while True:
            # Check if "k" value of the list equals to "val"
            if nums[k] == val:
                # Move the 2nd pointer back to 1 index
                i -= 1
                
                # Start an endless cycle
                while True:
                    # Check if the 2nd point is still greater 
                    # than the 1st one and if "i" value of 
                    # the list doesn't equals to "val"
                    if i > k and nums[i] != val:
                        # Swap values (move "val" value which is 
                        # in the "k" index to the "i" index)
                        nums[k], nums[i] = nums[i], nums[k]
                        # Break the cycle
                        break
                    else:
                        # Check if the 2nd pointer is still greater 
                        # than the 1st one
                        if i > k:
                            # Move the 2nd pointer back to 1 index    
                            i -= 1
                        else:
                            # Return amount of elements which are 
                            # not equal to "val"
                            return k
            
            # Move the 1st pointer next to 1 index
            k += 1
            
            # Check if both pointers are equal or if "k" value 
            # reached the length of the list
            if k == i or k >= len(nums):
                # Return amount of elements which are not equal 
                # to "val"
                return k
     
     
if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    print(Solution().removeElement(nums, val))
    
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(Solution().removeElement(nums, val))
    
    nums = [1]
    val = 1
    print(Solution().removeElement(nums, val))
    
    nums = [4, 5]
    val = 5
    print(Solution().removeElement(nums, val))