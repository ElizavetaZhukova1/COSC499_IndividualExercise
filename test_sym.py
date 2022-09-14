import unittest
from project_functions import calc_sym_words_ratio

class TestStringMethods(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(calc_sym_words_ratio(""), None)
    def test_whitespace(self):
        self.assertEqual(calc_sym_words_ratio("   "), None)
    def test_one_word(self):
        self.assertEqual(calc_sym_words_ratio("Hello"), 5)
    def test_many_words(self):
        self.assertEqual(calc_sym_words_ratio("Hello, how are you?I hope you are doing great!"), 3.5) 
    def test_punct(self):
        self.assertEqual(calc_sym_words_ratio("WaKe,, me up!!!When,september;ends..."), 4.167)
if __name__ == '__main__':
    unittest.main()