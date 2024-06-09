# Solved

# By 09.06.2024: 
# Runtime = 141 ms (better than 7.95% of users)
# Memory = 17.88 MB (better than 84.18% of users)
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Check if list is empty
        if len(nums) == 0:
            return 0
        
        # A variable to count unique values
        k = 1
        
        # Start an endless cycle
        while True:
            # Get current unique value
            unique_value = nums[k-1]
            
            # Start endless cycle
            while True:
                # Check if amount of unique values to search are 
                # less than the length of the list
                if k - 1 < len(nums) - 1:
                    # Check if "k" element equals to the unique 
                    # value
                    if nums[k] == unique_value:
                        # Remove the 'k' element and pull the rest
                        # of the list back to 1 index
                        nums.pop(k)
                    else:
                        # Increase amount of unique values
                        k += 1
                        # Breake the cycle
                        break
                
                else:
                    # Break the cycle
                    break
            
            # Check if amount of unique values equals to the 
            # length of the list
            if k == len(nums):
                # Return amount of unique values
                return k
        
# By 09.06.2024: 
# Runtime = 72 ms (better than 75.75% of users)
# Memory = 17.88 MB (better than 84.18% of users)
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Check if list is empty
        if len(nums) == 0:
            return 0
        
        # A variable to point to unique values
        k = 0
        
        # Start a cycle from the 1st element of the list to 
        # the length of the list (excluding)
        for i in range(1, len(nums)):
            # Check if current unique value doesn't equal to 
            # the "i" value
            if nums[k] != nums[i]:
                # Swap these values
                nums[k+1], nums[i] = nums[i], nums[k+1]
                # Go to the next unique value
                k += 1
        
        # Return amount of unique values    
        return k + 1
        
        
if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums))
    
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(nums))