from __future__ import unicode_literals

from syllables import Syllables
from tokenizer import Tokenizer

class Haiku:
    phrase_counts = (5, 7, 5)
    tokenizer = Tokenizer()

    def __init__(self, text):
        self.text = self.tokenizer.tokenize(text)
        self.phrases = self.phrases()

    def is_valid(self):
        return sum(Syllables(word).counts[0] for word in self.text) == sum(self.phrase_counts)

    def phrases(self):
        return ()
