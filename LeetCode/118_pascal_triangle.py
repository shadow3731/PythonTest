# Solved

# By 24.06.2024:
# Runtime = 38 ms (beats 49.11% of users)
# Memory = 16.46 MB (beats 80.39% of users)
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Create an empty list
        rows = []
        
        # A cycle to fill the outer list with lists of pascal 
        # triangle values on every step until "numRows"
        for i in range(1, numRows+1):
            # Create an empty list filled with 1 with length of 
            # "i"
            row = [1] * i
            
            # Check if current step is the 3rd or more. 
            # We don't need to fill the 1st 2 rows with other 
            # values distinct from 1
            if i >= 3:
                # A cycle to fill all the current row values, 
                # except of the 1st and the last. Because the 
                # 1st and the last values will always be 1
                for j in range(1, i-1):
                    # Define value of the current row value
                    row[j] = rows[-1][j-1] + rows[-1][j]
            
            # Add current row to the common list        
            rows.append(row)
        
        # Return list
        return rows
    
if __name__ == '__main__':
    numRows = 5
    print(Solution().generate(numRows))
    
    numRows = 1
    print(Solution().generate(numRows))