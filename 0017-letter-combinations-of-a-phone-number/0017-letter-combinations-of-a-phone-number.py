class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        keypad_mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        result = [""]

        for d in digits:
            new_result = []
            letters = keypad_mapping[d]
            
            for c in result:
                for l in letters:
                    new_result.append(c + l)

            result = new_result

        return result

