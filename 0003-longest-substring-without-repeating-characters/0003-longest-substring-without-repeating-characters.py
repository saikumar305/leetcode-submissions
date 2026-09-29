class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start , end = 0, 1
        curr = set()
        max_ =0

        for end in range(len(s)):

            while s[end] in curr:
                curr.remove(s[start])
                start+=1

            curr.add(s[end])

            max_ = max(max_, end-start+1)

        return max_





        