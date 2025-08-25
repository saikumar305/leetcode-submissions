class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(oc , cc , path):
            if len(path) == 2*n:
                res.append(path)
                return

            if oc < n:
                backtrack(oc+1, cc, path+"(")
            if cc < oc:
                backtrack(oc, cc+1, path+")")

        backtrack(0, 0, "")
        return res


        