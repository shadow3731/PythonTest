# Solved

# By 10.06.2024:
# Runtime = 43 ms (beats 20.35% of users)
# Memory = 16.43 MB (beats 91.28% of users)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Get length of the greater value
        max_length = len(a) if len(a) > len(b) else len(b)
        # Add zeros at the start depending on difference between 
        # "max_length" and the length of these 2 values
        a = '0'*(max_length-len(a)) + a
        b = '0'*(max_length-len(b)) + b
        # The binary sum of 2 values above
        c = ''
        # Extra value to sum
        extra = 0
        
        # Start a cycle from the last index of values to -1
        for i in range(max_length-1, -1, -1):
            # Sum "i" values of 2 binary numbers
            temp = int(a[i]) + int(b[i])
            
            # Check if sum is greater than 1
            if temp > 1:
                # Check if there's no extra value
                if extra == 0:
                    # Increase extra value
                    extra += 1
                    # Add zero at the start of the sum value
                    c = '0' + c
                else:
                    # Add one at the start of the sum value
                    c = '1' + c
            # Check if sum equals to 1
            elif temp == 1:
                # Check if there's no extra value
                if extra == 0:
                    # Add one at the start of the sum value
                    c = '1' + c
                else:
                    # Add zero at the start of the sum value
                    c = '0' + c
            else:
                # Check if there's no extra value
                if extra == 0:
                    # Add zero at the start of the sum value
                    c = '0' + c
                else:
                    # Decrease extra value
                    extra -= 1
                    # Add one at the start of the sum value
                    c = '1' + c
        
        # Check if there's an extra value
        if extra > 0:
            # Add one at the start of the sum value
            c = '1' + c
        
        # Return binary sum
        return c


if __name__ == '__main__':
    a = '11'
    b = '1'
    print(Solution().addBinary(a, b))
    
    a = '1010'
    b = '1011'
    print(Solution().addBinary(a, b))