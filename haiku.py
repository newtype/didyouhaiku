from __future__ import unicode_literals

from node import Node
from syllables import Syllables
from tokenizer import Tokenizer

class Haiku:
    phrase_counts = (5, 7, 5)
    max_syllables = sum(phrase_counts)
    tokenizer = Tokenizer()
    level_maxes = [5, 12, 17]

    def __init__(self, text):
        self.text = self.tokenizer.tokenize(text)
        self.phrases = self.phrases()

    def _is_valid(self, words, total=0, level=0):
        print words, total
        if (not words) and (total == self.level_maxes[-1]):
            print 'hello'
            return True
        if not words:
            return False
        if level == len(self.level_maxes):
            return False
        word = words[0]
        remnants = words[1:]
        for count in Syllables(word).counts:
            total += count
            if total > self.level_maxes[level]:
                continue
            elif total == self.level_maxes[level]:
                level += 1
            return self._is_valid(remnants, total, level)

    def is_valid(self):
        return self._is_valid(self.text)

    def is_valid2(self):
        return sum(Syllables(word).counts[0] for word in self.text) == sum(self.phrase_counts)

    def phrases(self):
        return ()
