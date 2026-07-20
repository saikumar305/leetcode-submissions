class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dicti = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}

        s1 = set()
        for  word in words:
            s =  ""
            for k in word:
                s += dicti[k]

            s1.add(s)
        return len(s1)
                
