# {{PROBLEM}} Function Design Recipe

A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.

## 1. Describe the Problem

```
A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.
```

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def make_snippet(string):
    """takes a string as argument and returns the first five words and then a '...'

    Parameters: (list all parameters and their types)
        string: a string containing words (e.g. "hello WORLD is my name and I am happy")

    Returns: (state the return value and its type)
        first five words and then a '...' (e.g. ["hello WORLD is my name..."])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
"""
given an empty string
returns empty string
"""
make_snippet("") => ""


"""
given fewer than five words
returns all words
"""
make_snippet("Hello world") => "Hello world"


"""
given more than five words 
returns five words and ...
"""
make_snippet("Hello my name is John and I am happy") => "Hello my name is John..."

```


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.make_snippet import *


"""
given an empty string
returns empty string
"""
def test_with_empty_string():
    actual = make_snippet("")
    expected = ""
    assert actual == expected

"""
given fewer than five words
returns all words
"""
def test_with_words_fewer_than_five_words():
    actual = make_snippet("Hello world")
    expected ="Hello world"
    assert actual == expected


"""
given more than five words 
returns five words and ...
"""
def test_with_words_more_than_five_words():
    actual = make_snippet("Hello my name is John and I am happy") 
    expected = "Hello my name is John..."
    assert actual == expected
```

Ensure all test function names are unique, otherwise pytest will ignore them!
