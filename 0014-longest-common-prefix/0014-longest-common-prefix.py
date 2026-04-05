class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]

        # for chars in zip(*strs):
        #     if len(set(chars)) == 1:
        #         prefix += chars[0]
        #     else:
        #         break
        # return prefix

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:len(prefix) -1]

        return prefix
                

        