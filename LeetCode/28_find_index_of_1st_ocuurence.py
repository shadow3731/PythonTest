# Solved

# By 10.06.2024:
# Runtime = 21 ms (beats 99.52% of users)
# Memory = 16.45 MB (beats 81.43% of users)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Return a value using built-in method
        return haystack.find(needle)

# By 10.06.2024:
# Runtime = 33 ms (beats 70.68% of users)
# Memory = 16.42 MB (beats 81.43% of users)    
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if needle is empty
        if needle == '':
            return -1
        
        # A variable to point to the 1st index of the needle 
        # in haystack
        first_index = 0
        # A variable to point to the current index of needle
        needle_index = 0
        # A variable to signal if the 1st letter of needle is found 
        # in the current index of haystack
        first_letter_found = False
        # A variable to save index of the 1st found letter after 
        # the signal
        first_letter_index = 0
        # A variable to point to index of every letter in haystack 
        # step-by-step
        i = 0
        
        # Start a cycle from "i" value to length of haystack
        while i < len(haystack):
            # Check if "i" index of haystack equals to 
            # "needle_index" of needle
            if haystack[i] == needle[needle_index]:
                # Check if the 1st letter of needle has been found 
                # before
                if first_letter_found is False:
                    # Make a signal that the first letter has been 
                    # found
                    first_letter_found = True
                    # Save the index of the 1st letter of needle 
                    # in haystack
                    first_letter_index = i
                
                # Save another index of the letter which equals 
                # to another index of haystack
                first_index = i
                # Increase index to search for equality between 
                # next letters in haystack and needle
                needle_index += 1
            else:
                # Check if there is a signal about finding the 
                # first equal letters in haystack and needle
                if first_letter_found is True:
                    # Remove the signal
                    first_letter_found = False
                    # Start search the occurence from the index 
                    # where it has been found for the first time
                    i = first_letter_index
                    # Reset the index of needle
                    needle_index = 0
            
            # Check if all the needle were found in haystack    
            if needle_index == len(needle):
                # Return the first index of the found needle 
                # in the haystack
                return first_index - needle_index + 1
            
            # Increase index to search for equality between next 
            # letters in haystack and needle
            i += 1
        
        # Return -1 if all the haystack were checked and no 
        # occurence with needle were found
        return -1
    

if __name__ == '__main__':
    haystack = 'sadbutsad'
    needle = 'sad'
    print(Solution().strStr(haystack, needle))
    
    haystack = 'leetcode'
    needle = 'leeto'
    print(Solution().strStr(haystack, needle))
    
    haystack = 'mississippi'
    needle = 'issip'
    print(Solution().strStr(haystack, needle))
    
    haystack = 'mississippi'
    needle = 'pi'
    print(Solution().strStr(haystack, needle))