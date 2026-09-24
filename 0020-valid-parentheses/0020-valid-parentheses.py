class Solution:
    def isValid(self, s: str) -> bool:
        mapper ={
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for i in s:
            if i in mapper.values():
                stack.append(i)
            else: 
                if stack and stack[-1] == mapper[i]:
                    stack.pop()
                else:
                    return False

        return not bool(stack)
        