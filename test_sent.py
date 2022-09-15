import unittest
from project_functions import calc_words_sent_ratio

class TestSentsCalculation(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(calc_words_sent_ratio("   "), None)
    def test_punct(self):
        self.assertEqual(calc_words_sent_ratio(".  ? ! ,& "), None)
    def test_one_sent(self):
        self.assertEqual(calc_words_sent_ratio("Have a great day"), 4)
    def test_many_sents(self):
        self.assertEqual(calc_words_sent_ratio("Who are you?I hope you are doing great! See you tomorrow...  Goodbye"), 3.25) 
if __name__ == '__main__':
    unittest.main()