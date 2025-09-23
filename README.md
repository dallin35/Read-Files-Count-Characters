## CODE 3 - Reading Files and Counting Words
## Instructions

This coding assignment asks you to create a program to read a file and obtain the frequency of words in its content.

Your program should include the following functions:

* `get_number_of_a`
  + The function should have **no parameters**
  + The function **returns** the number of times the letter **a** appears.
  + Note: your function should not be case sensitive (it should count both "a" and "A")
* `get_number_of_recommend`
  + The function should have **no parameters**
  + The function **returns** the number of times the letter **z** appears.
  + Note: your function should not be case sensitive (it should count both "z" and "Z")
* `get_number_of_free`
  + The function should have **no parameters**
  + The function **returns** the number of times the character **%** appears.
* `get_number_of_office`
  + The function should have **one parameter** (char)
  + The function **returns** the number of times the character passed in the parameter **char** appears.
  + Note: your function should not be case sensitive (it should count both lower and upper case versions of the character passed into the function)

## NOTE
* All of your functions should **iterate** through the file contents using a loop, **not** use the .count() function.

## Acknowledgments 

The original Office Product dataset was obtained from: https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/

Ni, J., Li, J., & McAuley, J. (2019, November). Justifying recommendations using distantly-labeled reviews and fine-grained aspects. In Proceedings of the 2019 conference on empirical methods in natural language processing and the 9th international joint conference on natural language processing (EMNLP-IJCNLP) (pp. 188-197).

Records of the original dataset were removed because of GitHub data size restrictions.