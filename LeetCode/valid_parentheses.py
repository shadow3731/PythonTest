class Solution:
    def isValid(self, s: str) -> bool:
        valid_open_parentheses = ['(', '[', '{']
        valid_close_parentheses = [')', ']', '}']
            
        while True:
            if s != '':
                if len(s) > 1:
                    i = 0
                    while i < len(s):
                        if s[i] in valid_open_parentheses and s[i+1] in valid_close_parentheses:
                            open_index = valid_open_parentheses.index(s[i])
                            close_index = valid_close_parentheses.index(s[i+1])
                            if open_index == close_index:
                                s1, s2 = s[:i], s[i+2:]
                                s = s1 + s2
                                break
                            else:
                                return False
                        elif s[i] in valid_open_parentheses and s[i+1] in valid_open_parentheses and i+1 != len(s)-1:
                            i += 1
                        else:
                            return False
                else:
                    return False
            else:
                return True
            
            
if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("({)}")) 
    print(solution.isValid("{[]}"))
    print(solution.isValid("(){}}{"))
    print(solution.isValid("[({(())}[()])]"))
    print(solution.isValid("[([]])"))
    print(solution.isValid("(("))