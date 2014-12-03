import unittest

from haiku import Haiku

class TestHaiku(unittest.TestCase):
    def setUp(self):
        self.valid_haiku = Haiku('at the age old pond a frog leaps into water a deep resonance')
        self.valid_haiku_multiple_prons = Haiku('word word probably {0}'.format('word ' * 12))
        self.invalid_haiku = Haiku('at the age old pond')
        self.tricky_invalid_haiku = Haiku('word word word elephant {0}'.format('word ' * 11))

    def test_invalid_haiku(self):
        self.assertFalse(self.invalid_haiku.is_valid())

    def test_valid_haiku(self):
        self.assertTrue(self.valid_haiku.is_valid())

    def test_valid_haiku_multiple_prons(self):
        self.assertTrue(self.valid_haiku_multiple_prons.is_valid())

    def test_right_syllables_wrong_phrasing(self):
        """ a potential haiku can have 17 syllables but a word that breaks
            between lines
        """
        self.assertFalse(self.tricky_invalid_haiku.is_valid())

    def test_phrase_splitting(self):
        self.assertEqual(
            self.valid_haiku.to_s(),
            'at the age old pond / a frog leaps into water / a deep resonance'
        )

    def test_phrase_splitting_multiple_prons(self):
        text = 'If you favorite that last tweet of mine you are the scum I called out'
        haiku = Haiku(text)
        self.assertEqual(
            haiku.to_s(),
            'If you favorite / that last tweet of mine you are / the scum I called out'
        )


if __name__ == '__main__':
    unittest.main()
