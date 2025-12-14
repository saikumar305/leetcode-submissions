class Solution:
    def get_vowel_count(self, word):
        vowels = "aeiou"
        c = 0
        for w in word:
            if w in vowels:
                c+=1

        return c

    def reverseWords(self, s: str) -> str:
        vowels = "aeiou"
        words = s.split(" ")
        c = 0
        first_vc = 0
        first_vc = self.get_vowel_count(words[0])
        
        op = [words[0]]
        for word in words[1:]:
            c = self.get_vowel_count(word)
            if c == first_vc:
                op.append(word[::-1])
            else:
                op.append(word)

        
        return " ".join(op)





        