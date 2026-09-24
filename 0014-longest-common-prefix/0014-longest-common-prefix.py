class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        short = min(strs, key=len)

        for i in range(len(short)):
            for j in strs:
                if short[i] != j[i]:
                    return short[:i]


        return short

    
        