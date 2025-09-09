class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnNumber=0
        for c in columnTitle:
            columnNumber=columnNumber*26+ord(c)-ord('A')+1
        return columnNumber