import unittest

from syllables import Syllables

class TestSyllables(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_count_unique_result(self):
        syl = Syllables('hello')
        self.assertIn(2, syl.counts)
        self.assertEqual(len(syl.counts), 1)
        
    def test_count_multiple_results(self):
        syl = Syllables('probably')
        self.assertIn(2, syl.counts)
        self.assertIn(3, syl.counts)
        self.assertEqual(len(syl.counts), 2)

    def test_count_no_results(self):
        syl = Syllables('mytzlplk')
        self.assertEquals(len(syl.counts), 0)
        

if __name__ == '__main__':
    unittest.main()
