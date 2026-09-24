class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        short = min(strs, key=len)
        val = ""

        for i in range(len(short)):
            for j in strs:
                if short[i] == j[i]:
                    continue

                else:
                    return val
                    
            val += short[i]
        return val

    
        