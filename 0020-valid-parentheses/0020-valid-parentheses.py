class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False

        mapper = {')': '(', ']': '[', '}': '{'}
        stack = []

        for i in s:
            
            if i in '{([':
                stack.append(i)
            else:
                
                if stack:
                    if stack[-1] == mapper[i]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                    
        return len(stack) == 0

        