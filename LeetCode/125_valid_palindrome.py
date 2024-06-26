# Solved

# By 26.06.2024:
# Runtime = 42 ms (beats 73.07% of users)
# Memory = 18.12 MB (beats 17.99% of users)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Import a function from the module
        from re import sub
        # Lowercase the string and remove all the 
        # non-alphanumeric characters
        s = sub(r'[^a-zA-Z0-9]', '', s.lower())
        
        # Check if new string is a palindrome
        return s == s[::-1]
    
if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))
    
    s = "race a car"
    print(Solution().isPalindrome(s))
    
    s = " "
    print(Solution().isPalindrome(s))
    
    s = "ab_a"
    print(Solution().isPalindrome(s))