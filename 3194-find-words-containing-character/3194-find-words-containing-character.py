class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        op = []
        for i, word in enumerate(words):
            if x in word:
                op.append(i)

        return op

        