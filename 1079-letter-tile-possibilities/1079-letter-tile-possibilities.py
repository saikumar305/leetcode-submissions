from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = Counter(tiles)

        def backtrack():
            total = 0

            for char in freq:
                if freq[char] > 0:
                    total +=1
                    freq[char] -=1

                    total+= backtrack()

                    freq[char] +=1

            return total

        return backtrack()

        