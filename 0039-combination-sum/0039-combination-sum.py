class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res= []

        def backtrack(i , curr, path):

            if (i ==len(candidates) and curr !=0) or curr < 0:
                return
            
            if  curr == 0:
                res.append(path[:])
                return
            
            path.append(candidates[i])
            backtrack(i, curr - candidates[i], path)
            path.pop()
            backtrack(i+1 , curr, path)

        backtrack(0, target, [])

        return res


            

        