""" Count the possible number of syllables in a word or words.
"""
from __future__ import unicode_literals

from nltk.corpus import cmudict

class Syllables:
    CMU = cmudict.dict()
    
    def __init__(self, word):
        self.word = word
        self.counts = self._count()

    def _count_syllables(self, pron):
        return len([syl for syl in pron if syl[-1].isdigit()])

    def _count_CMU(self, word):
        """ Use CMU pronunciation dictionary to return the number of
            syllables are in a word.
        """
        pronunciations = self.CMU.get(word.lower())
        if not pronunciations:
            return []
        syllable_counts = [self._count_syllables(pron) for pron in pronunciations]
        return list(set(syllable_counts))

    def _count(self):
        """ Return a list of the syllable counts for a word."""
        return self._count_CMU(self.word)

