class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        freq = []
        for word in words:
            temp = [0] * 26
            for ch in word:
                temp[ord(ch) - ord('a')] += 1
            freq.append(temp)
        res = []
        for i in range(26):
            possibility = float('inf')
            for j in range(n):
                possibility = min(possibility, freq[j][i])
            for k in range(possibility):
                res.append(chr(ord('a') + i))
        return res
        