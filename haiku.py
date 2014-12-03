from __future__ import unicode_literals

from node import Node
from syllables import Syllables
from tokenizer import Tokenizer

class Haiku:
    phrase_counts = (5, 7, 5)
    tokenizer = Tokenizer()
    level_maxes = [5, 12, 17]

    def __init__(self, text):
        self.text = self.tokenizer.tokenize(text)
        self.phrases = [[], [], []]
        self.__is_valid = None

    def _is_valid(self, words, total=0, level=0):
        if (not words) and (total == self.level_maxes[-1]):
            return True
        if not words:
            return False
        if level == len(self.level_maxes):
            return False
        word = words[0]
        remnants = words[1:]

        for count in Syllables(word).counts:
            current_total = total + count
            if current_total > self.level_maxes[level]:
                continue

            self.phrases[level].append(word)
            if current_total == self.level_maxes[level]:
                level += 1
            result = self._is_valid(remnants, current_total, level)
            if result:
                return True

        return False

    def is_valid(self):
        if self.__is_valid is None:
            self.__is_valid = self._is_valid(self.text)

        return self.__is_valid

    def to_s(self):
        self.is_valid()
        return ' / '.join(' '.join(self.phrases[i]) for i in xrange(len(self.phrases)))

    def is_valid2(self):
        return sum(Syllables(word).counts[0] for word in self.text) == sum(self.phrase_counts)
