# Solved

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Check if the length of the list is less than 1 element 
        # or more than 200 elements
        if len(strs) < 1 or len(strs) > 200:
            return ''
        
        # Expression for checking if the length of list values
        # is more than 0 and less or equal to 200
        val_length_gen_exp = (
            len(s) > 0 and len(s) <= 200 for s in strs
        )
        # Expression for checking if list values contain only 
        # lowecase symbols
        low_case_gen_exp = (s.islower() for s in strs)
        
        # Check both upper expressions
        if not all(val_length_gen_exp) or not all(low_case_gen_exp):
            return ''
        
        # A value to contain the common prefix
        common_prefix = ''
        # A value to point to the last letter of expected prefix
        index = 1
        
        # Start endless cycle
        while True:
            # Expression for checking if the prefix of every 
            # list value equals to the prefix of the 1st list value.
            # The prefix length is defined from the 1st letter 
            # to value of "index" variable
            prefix_gen_exp = (
                s[:index] == strs[0][:index] for s in strs
            )
            
            # If upper expression is True...
            if all(prefix_gen_exp):
                # Save expected prefix and use it next
                common_prefix = strs[0][:index]
                # Increase prefix length
                index += 1
                
                # If value of "index" variable is more than 
                # the length of the 1st list value...
                if index > len(strs[0]):
                    # Return the last saved prefix
                    return common_prefix
            
            else:
                # Return the last saved prefix           
                return common_prefix
        

if __name__ == '__main__':
    strs = [
        ['flower', 'flow', 'flight'],
        ["dog","racecar","car"],
        [''],
        ['a'],
        ['ab', 'a']
    ]
    
    for s in strs:
        print(Solution().longestCommonPrefix(s))