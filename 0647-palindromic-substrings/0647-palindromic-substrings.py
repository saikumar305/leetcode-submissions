class Solution:
    def countSubstrings(self, s: str) -> int:
        # c = 0
        # def ispalindrome(ss):
        #     return ss == ss[::-1]
        
        # res = []
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if ispalindrome(s[i:j+1]):
        #             c+=1
        

        # return c

        if len(s) <= 1:
            return len(s)

        def expand_from_center(left, right):
            c = 0
            while left>=0 and right < len(s) and s[left] == s[right]:

                c +=1
                left -=1
                right +=1
            return  c

        max_str = s[0]
        count = 0
        for i in range(len(s)):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i+1)
            count += (odd +even)

        return count