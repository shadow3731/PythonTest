# Solved

# By 12.06.2024:
# Runtime = 29 ms (beats 87.35% of users)
# Memory = 16.46 MB (beats 71.92% of users)
class Solution:
    def climbStairs(self, n: int) -> int:
        # Check if "n" equals to 0 or 1
        if n == 0 or n == 1:
            # Return n 
            return n
        
        # The 1st term
        x = 1
        # The 2nd term
        y = 1
        # The sum
        z = 1
        
        # The sum equals to the value from Fibonacci's sequence 
        # at n-1 index
        for _ in range(2, n+1):
            # Get the 2nd term from the previous step
            x = y
            # Get the sum from the previous step
            y = z
            # Get new sum
            z = y + x
        
        # Return amount
        return z
        
            
if __name__ == '__main__':
    n = 2
    print(Solution().climbStairs(n))
    
    n = 3
    print(Solution().climbStairs(n))