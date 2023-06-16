#!/usr/bin/env python3

#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def __init__(self):
        self.s = input('Enter string: ')

    def isValid(self):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        
        for char in self.s:
            if char in brackets:
                stack.append(char)
            elif char in brackets.values():
                if len(stack) == 0 or brackets[stack.pop()] != char:
                    return False
        
        return len(stack) == 0

test1 = Solution()
print(test1.isValid())

