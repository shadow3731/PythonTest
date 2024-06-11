# Solved

# By 11.06.2024:
# Runtime = 2108 ms (beats 5.00% of users)
# Memory = 16.46 MB (beats 79.02% of users)
class Solution:
    # This method just get every integer acsending and starting 
    # from 0, and check if target value is in the boundaries 
    # between i value and i+1 value.
    def mySqrt(self, x: int) -> int:
        # Start calculate from zero
        value = 0
        
        # Start an endless cycle
        while True:
            # Check if current value suits between 2 neighbour 
            # values
            if x >= value * value and x < (value+1) * (value+1):
                # Return value
                return value
            # Increase value
            value += 1

# By 11.06.2024:
# Runtime = 39 ms (beats 61.71% of users)
# Memory = 16.72 MB (beats 6.15% of users)           
class Solution:
    # Using Heron's method
    def mySqrt(self, x: int) -> int:
        # Calculate the initial approximation. 
        # If "x" is less than 10, take 2, otherwise 6
        a = 2 if x < 10 else 6
        # Define accuracy
        eps = 0.1
        # Calculate the 1st possible value
        x_0 = a * 100
        
        # Start an endless cycle
        while True:
            # Calculate next possible value
            x_1 = (x_0 + x/x_0) / 2
            
            # Check if absolute difference of 2 possible values 
            # is less than the accuracy value
            if abs(x_1 - x_0) <= eps:
                # Return the 2nd possible value as an integer 
                # value
                return int(x_1)
            
            # Set new 1st possible value
            x_0 = x_1
            
            
if __name__ == '__main__':
    x = 4
    print(Solution().mySqrt(x))
    
    x = 8
    print(Solution().mySqrt(x))
    
    x = 125348
    print(Solution().mySqrt(x))