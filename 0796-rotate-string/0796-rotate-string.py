class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        # for i in range(len(s)):
        #     matcher = s_copy[i:]+s_copy[:i] 

        #     if goal == matcher:
        #         return True

        # return False
        return goal in s+s


        