class Solution:
    def isValid(self, s):
        stack = [0]
        mapping = {0: None, '(':')', '[':']', '{':'}'}
        for char in s:
            if char in mapping: 
                stack.append(char)
            else:
                if mapping[stack.pop()] != char: return False
        return stack == [0]
