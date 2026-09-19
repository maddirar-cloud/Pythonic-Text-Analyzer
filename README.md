**Overview**

This is a refactor project that refactors a poorly written script (unpythonic_analyzer.py) into a cleaner, more efficient and Pythonic program (text_analyzer.py). Both scripts analyze a text file and report several key things:

1. Total Number of Words
2. Number of Unique Words
3. Five Most Frequent Words
4. Number of Words Longer Than 3 Words

**Screencast**:
Watch the project walkthrough here: 

**Requirements**:
Python 3.6 or newer
No third-party packages. Utilizes standard library

**How to Run**:
Clone the repository
Make sure sample.txt is in the same folder as the scripts
Run refactored script

**Expected Output**:
Running either script on the provided sample.txt should give:

The total number of words is: 216
The unique words count is: 117
The most frequent words are:
'the': 22
'and': 13
'is': 11
'code': 11
'a': 9
Long words (more than 3 characters): 140

**Refactorization**
Several improvements were made:
1. PEP 8 Compliance. Variables are consistent to snake_case.
2. Context Manager. Replaced manual open()/close() calls with a "with" statement.
3. List Comprehension. for-loops are now replaced with shorter 1 line iterators.

**Author**
Ram Maddirala
