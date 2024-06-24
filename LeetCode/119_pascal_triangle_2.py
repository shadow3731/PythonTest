# Solved

# By 24.06.2024:
# Runtime = 45 ms (beats 5.66% of users)
# Memory = 16.27 MB (beats 99.36% of users)
from typing import List


class Solution:
    # Calculate every value using the expression with factorial
    def getRow(self, rowIndex: int) -> List[int]:
        from math import factorial
        return [factorial(rowIndex) // (factorial(r)*factorial(rowIndex-r)) for r in range(rowIndex+1)]

# By 24.06.2024:
# Runtime = 31 ms (beats 81.46% of users)
# Memory = 16.33 MB (beats 94.10% of users)    
class Solution:
    # Calculate every value using another expression
    def getRow(self, rowIndex: int) -> List[int]:
        # Create a list of ones
        row = [1] * (rowIndex + 1)
        
        # A cycle to calculate every value, starting from 
        # the 2nd and skipping the last one
        for i in range(1, rowIndex):
            row[i] = row[i - 1] * (rowIndex - i + 1) // i
        
        return row

if __name__ == '__main__':
    rowIndex = 3
    print(Solution().getRow(rowIndex))
    
    rowIndex = 1
    print(Solution().getRow(rowIndex))