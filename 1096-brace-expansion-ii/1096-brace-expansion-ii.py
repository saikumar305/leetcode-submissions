from typing import List

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        return sorted(self.dfs(expression))

    def dfs(self, expr: str):
        parts = self.split_by_comma(expr)
        result = set()

        for part in parts:
            curr = [""]   # for concatenation
            i = 0

            while i < len(part):
                if part[i] == '{':
                    j = self.find_closing(part, i)
                    sub = self.dfs(part[i+1:j])
                    curr = self.product(curr, sub)
                    i = j + 1
                else:
                    curr = [c + part[i] for c in curr]
                    i += 1

            result.update(curr)

        return result

    def split_by_comma(self, expr: str):
        parts = []
        depth = 0
        start = 0

        for i, ch in enumerate(expr):
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
            elif ch == ',' and depth == 0:
                parts.append(expr[start:i])
                start = i + 1

        parts.append(expr[start:])
        return parts

    def find_closing(self, s: str, i: int):
        depth = 0
        for j in range(i, len(s)):
            if s[j] == '{':
                depth += 1
            elif s[j] == '}':
                depth -= 1
                if depth == 0:
                    return j

    def product(self, list1, list2):
        return [a + b for a in list1 for b in list2]