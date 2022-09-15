# COSC499 Individual exercise: calculating the simple text statistics using Python

The list of features:

1. Calculate the average number of symbols per word
2. Calculate the average number of words per sentence

## Quickstart

1. Download the code from the repository or clone the repository on your machine
2. Run `project_run.py` in python terminal
3. Then prompted for input enter any text string. For example, try _I tell you: one must have chaos in one, to give birth to a dancing star. I tell you: you still have chaos in you._ (For the sake of academic integrity, that's from Friedrich Nietzsche, Thus Spoke Zarathustra)

- - - -

## Feature description

### Feature 1

This function (`calc_sym_words_ratio()` from `project_functions.py`) first lowercases the text, preprocesses it using re (pre-installed python package) to get rid of the punctuation signs, tokenizes the string into words and then calculates the total amount of symbols and divides it by total amount of words, rounding the final result to 3 decimal places. The function is well-equipped to deal with punctuation signs, double whitespaces, and the absence of whitespaces after punctuation signs (for example "Well,then" will be interpreted as 2 words), but it does not expand contractions ("They're" will be interpreted as 1, 7-letter word). The punctuation signs and whitespaces are not included in the symbols count.

### Feature 2

This function (`calc_words_sent_ratio()` from `project_functions.py`) breaks the user's input into sentences and, separately, breaks it into words (both are performed using re Python package). Then it divides the number of words by the number of sentences and returns the result rounded to 3 decimal places.
- - - -

## Description of each file

- `project_functions.py` contains all the functions needed for the project to run (contains the functions needed for both features)
- `project_run.py` takes the user input and by using the functions from `project_functions.py` prints to the user the statistics about the text she entered
- `test_sym.py` implements unit tests for the first feature using unittest (pre-installed python package)
- `test_sent.py` implements unit tests for the second feature using unittest (pre-installed python package)
- `explanation.md` explanation for tests, as required by the assignment
