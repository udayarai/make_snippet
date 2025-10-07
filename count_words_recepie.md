# {{PROBLEM}} Function Design Recipe

A function called count words that takes a string as an argument and returns the number of words in that string.


## 1. Describe the Problem

```
count words needs to take in a string as an argument and return the number of words in that string
```

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def count_words(string):
    """takes a string as argument and returns the number of words in the string

    Parameters: (list all parameters and their types)
        string: a string containing words (e.g. "hello WORLD is my name and I am happy")

    Returns: (state the return value and its type)
        returns the number of words (e.g. string "hello WORLD is my name and I am happy" will return 9)

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
"""
given an empty string
returns number of words
"""
count_words("") => 0


"""
given fewer than five words
returns number of words
"""
count_words("Hello world") => 2


"""
given more than five words 
returns the length
"""
count_words("Hello my name is John and I am happy") => 9

"""
given numbers seperated by spaces
returns the length
"""
count_words("1234 4343 3432") => 3
```


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.count_words import *


"""
given an empty string
returns number of words
"""
def test_with_empty_string():
    actual = count_words("")
    expected = 0
    assert actual == expected

"""
given fewer than five words
returns number of words
"""
def test_with_words_fewer_than_five_words():
    actual = count_words("Hello world")
    expected = 2
    assert actual == expected


"""
given more than five words 
returns number of words
"""
def test_with_words_more_than_five_words():
    actual = count_words("Hello my name is John and I am happy") 
    expected = 9
    assert actual == expected

"""
given numbers seperated by spaces
returns the length
"""
def test_with_numbers_seperated_by_spaces():
    actual = count_words("1234 4343 3432") 
    expected = 3
    assert actual == expected
```

Ensure all test function names are unique, otherwise pytest will ignore them!
