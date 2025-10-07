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