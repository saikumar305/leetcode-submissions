class Solution:
    def scoreBalance(self, s: str) -> bool:
        a_dict = {chr(i + 96): i for i in range(1, 27)}

        for i in range(1, len(s)):
            left = s[0:i]
            right = s[i:]

            sum_left = sum([a_dict[c] for c in left])
            sum_right = sum([a_dict[c] for c in right])

            if sum_left == sum_right:
                return True
            
        return False



        