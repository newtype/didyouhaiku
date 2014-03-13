import unittest

from haiku import Haiku

class TestHaiku(unittest.TestCase):
    def setUp(self):
        self.valid_haiku = Haiku('at the age old pond a frog leaps into water a deep resonance')
        self.invalid_haiku = Haiku('at the age old pond')
        self.tricky_invalid_haiku = Haiku('word word word elephant {0}'.format('word ' * 11))

    def test_invalid_haiku(self):
        self.assertFalse(self.invalid_haiku.is_valid())

    def test_valid_haiku(self):
        self.assertTrue(self.valid_haiku.is_valid())

    def test_right_syllables_wrong_phrasing(self):
        """ a potential haiku can have 17 syllables but a word that breaks
            between lines
        """
        self.assertFalse(self.tricky_invalid_haiku.is_valid())

    def test_phrase_splitting(self):
        pass

if __name__ == '__main__':
    unittest.main()
