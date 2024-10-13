import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # word_count = {}
        # paragraph = re.sub(r'[^\w\s]', '', paragraph)

        # for word in paragraph.lower().split(" "):
        #     word_count[word] = word_count.get(word,0) + 1
            
        # freq_word = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
        # print(freq_word)
        # for w in freq_word.keys():
        #     if w in banned:
        #         continue
        #     else:
        #         return w
        # Step 1: Convert to lowercase and replace punctuation with spaces
        normalized_paragraph = re.sub(r'[^\w\s]', ' ', paragraph.lower())
        
        # Step 2: Tokenize the paragraph into words
        words = normalized_paragraph.split()
        
        # Step 3: Filter out the banned words and count the frequency of the remaining words
        banned_set = set(banned)
        word_counts = Counter(word for word in words if word not in banned_set)
        
        # Step 4: Find the most common word that is not banned
        most_common_word, _ = word_counts.most_common(1)[0]
        
        return most_common_word
            