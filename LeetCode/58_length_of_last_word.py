# Solved

# By 10.06.2024:
# Runtime = 30 ms (beats 84.88% of users)
# Memory = 16.48 MB (beats 95.70% of users)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Check if string is empty
        if s == '':
            return 0
        
        # Remove whitespace at the end of the string using 
        # built-in method
        s = s.rstrip()
        # Split string into separate words by whitespaces using 
        # built-in method and return the length of the last word
        return len(s.split(' ')[-1])
    
    
if __name__ == '__main__':
    s = "Hello World"
    print(Solution().lengthOfLastWord(s))
    
    s = "   fly me   to   the moon  "
    print(Solution().lengthOfLastWord(s))
    
    s = "luffy is still joyboy"
    print(Solution().lengthOfLastWord(s))