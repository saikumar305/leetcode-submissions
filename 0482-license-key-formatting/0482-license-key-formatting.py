class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-','').upper()
        start = len(s)%k or k
        res = [s[:start]]

        for i in range(start, len(s), k):
            res.append(s[i:i+k])
        
        return '-'.join(res)