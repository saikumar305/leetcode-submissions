class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {}

        for char in magazine:
            map[char] = map.get(char, 0) + 1

        for char in ransomNote:
            if char in map and map[char] > 0:
                map[char] -= 1
            else:
                return False
            
        return True

        