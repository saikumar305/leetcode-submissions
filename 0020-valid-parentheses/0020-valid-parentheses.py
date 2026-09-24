class Solution:
    def isValid(self, s: str) -> bool:
        mapper ={
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for i in s:
            if i in mapper:
                if not stack or stack[-1] != mapper[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
                    
        return not stack
        