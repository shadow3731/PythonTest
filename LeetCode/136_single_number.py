# Solved

# By 26.06.2024:
# Runtime = 101 ms (beats 92.67% of users)
# Memory = 19 MB (beats 54.28% of users)
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Set initial value
        result = 0
        
        # A cycle to go through every value of the list
        for num in nums:
            # Make xor operation on every value. So that only 
            # a single value will stay
            result ^= num
        
        # Return a unique value
        return result
        
if __name__ == '__main__':
    nums = [2, 2, 1]
    print(Solution().singleNumber(nums))
    
    nums = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(nums))
    
    nums = [1]
    print(Solution().singleNumber(nums))