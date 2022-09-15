# Here are the explanations for the test cases

## `test_sym.py` (first feature)

- The first 2 tests (`test_empty` and `test_whitespace`) should return None as their inputs do not contain any words. This test makes sure that the edge case is handled correctly
- `test_one_word` tests the simplest case there an input is just one word "Hello" so the required output is 5 (5 letters divided by 1 word)
- `test_many_words` tests the case there where are a lot of words. The provided input "Hello, how are you?I hope you are doing great!" contains 35 letters and 10 words, so the required output is 3.5
- `test_punct` makes sure my program can handle punctuation correctly. The input "WaKe,, me up!!!When,september;ends..." contains 6 words and 25 letters, so the required output is 4.167

## `test_sent.py` (second feature)

- The first 2 tests (`test_empty` and `test_punct`) should return None as their inputs do not contain any sentences. This test makes sure that the edge case is handled correctly
- `test_one_sent` tests the simplest case there an input is just one sentence "Have a great day" so the required output is 4 (4 words divided by 1 sentence)
- `test_many_sents` tests the case there where are a lot of sentences. The provided input "Who are you?I hope you are doing great! See you tomorrow...  Goodbye" contains 13 words and 4 sentences, so the required output is 3.25
